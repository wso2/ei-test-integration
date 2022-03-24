#!/bin/bash
#----------------------------------------------------------------------------
#  Copyright (c) 2020 WSO2, Inc. http://www.wso2.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#----------------------------------------------------------------------------
set -o xtrace; set -e

TESTGRID_DIR=/opt/testgrid/workspace
INFRA_JSON='infra.json'
PRODUCT_REPOSITORY=$1
PRODUCT_REPOSITORY_BRANCH=$2
PRODUCT_NAME=$3
PRODUCT_VERSION=$4
PRODUCT_REPOSITORY_NAME=$(echo $PRODUCT_REPOSITORY | rev | cut -d'/' -f1 | rev | cut -d'.' -f1)
PRODUCT_REPOSITORY_PACK_DIR="$TESTGRID_DIR/$PRODUCT_REPOSITORY_NAME/distribution/target"
INT_TEST_MODULE_DIR="$TESTGRID_DIR/$PRODUCT_REPOSITORY_NAME/integration"
# cloud formation properties
CFN_PROP_FILE="${TESTGRID_DIR}/cfn-props.properties"
JDK_TYPE=$(grep -w "JDK_TYPE" ${CFN_PROP_FILE} | cut -d"=" -f2)
DB_TYPE=$(grep -w "DB_TYPE" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_VERSION=$(grep -w "CF_DB_VERSION" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_PASSWORD=$(grep -w "CF_DB_PASSWORD" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_USERNAME=$(grep -w "CF_DB_USERNAME" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_HOST=$(grep -w "CF_DB_HOST" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_PORT=$(grep -w "CF_DB_PORT" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_NAME=$(grep -w "SID" ${CFN_PROP_FILE} | cut -d"=" -f2)
REMOTE_PACK_NAME=$(grep -w "REMOTE_PACK_NAME" ${CFN_PROP_FILE} | cut -d= -f2)
function log_info(){
    echo "[INFO][$(date '+%Y-%m-%d %H:%M:%S')]: $1"
}

function log_error(){
    echo "[ERROR][$(date '+%Y-%m-%d %H:%M:%S')]: $1"
    exit 1
}

function install_jdk(){
    jdk_name=$1

    mkdir -p /opt/${jdk_name}
    jdk_file=$(jq -r '.jdk[] | select ( .name == '\"${jdk_name}\"') | .file_name' ${INFRA_JSON})
    wget -q https://integration-testgrid-resources.s3.amazonaws.com/lib/jdk/$jdk_file.tar.gz
    tar -xzf "$jdk_file.tar.gz" -C /opt/${jdk_name} --strip-component=1

    export JAVA_HOME=/opt/${jdk_name}
    echo $JAVA_HOME
}

source /etc/environment

log_info "Clone Product repository"
git clone https://$PRODUCT_REPOSITORY $TESTGRID_DIR/${PRODUCT_REPOSITORY_NAME} --branch $PRODUCT_REPOSITORY_BRANCH

log_info "Exporting JDK"
install_jdk ${JDK_TYPE}

if [[ ${DB_TYPE} == "oracle-se2" ]]; then
    # export env for oracle-19
    export TestGrid=true
    export oracle_url="jdbc:oracle:thin:@${CF_DB_HOST}:1521/${CF_DB_NAME}"
    export oracle_user="MI_DB"
    export oracle_pwd="${CF_DB_PASSWORD}"
fi

mkdir -p $PRODUCT_REPOSITORY_PACK_DIR

log_info "Copying product pack to Repository"
[ -f $TESTGRID_DIR/$REMOTE_PACK_NAME.zip ] && rm -f $TESTGRID_DIR/$REMOTE_PACK_NAME.zip
cd $TESTGRID_DIR && zip -qr $REMOTE_PACK_NAME.zip $REMOTE_PACK_NAME
mv $TESTGRID_DIR/$REMOTE_PACK_NAME.zip $PRODUCT_REPOSITORY_PACK_DIR/.

if [[ ${DB_TYPE} == "oracle-se2" ]]; then
    cd $INT_TEST_MODULE_DIR  && mvn clean install -P db-tests -fae -B -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn
else
    cd $INT_TEST_MODULE_DIR  && mvn clean install -fae -B -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn
fi
