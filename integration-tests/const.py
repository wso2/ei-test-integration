# Copyright (c) 2018, WSO2 Inc. (http://wso2.com) All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

NS = {'d': 'http://maven.apache.org/POM/4.0.0'}
ZIP_FILE_EXTENSION = ".zip"
CARBON_NAME = "carbon.zip"
VALUE_TAG = "{http://maven.apache.org/POM/4.0.0}value"
SURFACE_PLUGIN_ARTIFACT_ID = "maven-surefire-plugin"
DATASOURCE_PATHS = {"product-apim": {},
                    "product-is": {},
                    "product-ei": {"CORE": ["conf/datasources/master-datasources.xml"],
                                   "BROKER": ["wso2/broker/conf/datasources/master-datasources.xml",
                                              "wso2/broker/conf/datasources/metrics-datasources.xml"],
                                   "BPS": ["wso2/business-process/conf/datasources/master-datasources.xml",
                                           "wso2/business-process/conf/datasources/bps-datasources.xml",
                                           "wso2/business-process/conf/datasources/activiti-datasources.xml"]},
                    }
M2_PATH = {"product-is": "is/wso2is", "product-apim": "am/wso2am",
           "product-ei": "ei/wso2ei"}
DIST_POM_PATH = {"product-is": "modules/distribution/pom.xml", "product-apim": "modules/distribution/product/pom.xml",
                 "product-ei": "distribution/pom.xml"}
LIB_PATH = "lib"
DISTRIBUTION_PATH = {"product-apim": "modules/distribution/product/target",
                     "product-is": "modules/distribution/target",
                     "product-ei": "distribution/target"}
PRODUCT_STORAGE_DIR_NAME = "storage"
TEST_PLAN_PROPERTY_FILE_NAME = "testplan-props.properties"
INFRA_PROPERTY_FILE_NAME = "infrastructure.properties"
LOG_FILE_NAME = "integration.log"
ORACLE_DB_ENGINE = "ORACLE-SE2"
MSSQL_DB_ENGINE = "SQLSERVER-SE"
MYSQL_DB_ENGINE = "MYSQL"
DEFAULT_ORACLE_SID = "orcl"
DEFAULT_DB_USERNAME = "wso2carbon"
LOG_STORAGE = "logs"
LOG_FILE_PATHS = {"product-apim": [],
                  "product-is": [],
                  "product-ei": []}
DB_META_DATA = {
    "MYSQL": {"prefix": "jdbc:mysql://", "driverClassName": "com.mysql.jdbc.Driver", "jarName": "mysql.jar",
              "DB_SETUP": {
                  "product-apim": {},
                  "product-is": {},
                  "product-ei": {"WSO2_CARBON_DB_CORE": ['dbscripts/mysql5.7.sql'],
                                 "WSO2_CARBON_DB_BROKER": ['wso2/broker/dbscripts/mysql5.7.sql'],
                                 "WSO2_CARBON_DB_BPS": ['wso2/business-process/dbscripts/mysql5.7.sql'],
                                 "WSO2_MB_STORE_DB_BROKER": ['wso2/broker/dbscripts/mb-store/mysql-mb.sql'],
                                 "WSO2_METRICS_DB_BROKER": ['wso2/broker/dbscripts/metrics/mysql.sql'],
                                 "BPS_DS_BPS": ['wso2/business-process/dbscripts/bps/bpel/create/mysql.sql'],
                                 "ACTIVITI_DB_BPS": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.mysql.create.identity.sql'],
                                }}},

    "SQLSERVER-SE": {"prefix": "jdbc:sqlserver://",
                     "driverClassName": "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jarName": "sqlserver-ex.jar",
                     "DB_SETUP": {
                         "product-apim": {},
                         "product-is": {},
                         "product-ei": {"WSO2_CARBON_DB_CORE": ['dbscripts/mssql.sql'],
                                        "WSO2_MB_STORE_DB": ['wso2/broker/dbscripts/mb-store/mssql-mb.sql'],
                                        "BPS_DS": ['wso2/business-process/dbscripts/bps/bpel/create/mssql.sql'],
                                        "ACTIVITI_DB": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.mssql.create.identity.sql']}}},

    "ORACLE-SE2": {"prefix": "jdbc:oracle:thin:@", "driverClassName": "oracle.jdbc.OracleDriver",
                   "jarName": "oracle-se.jar",
                   "DB_SETUP": {
                       "product-apim": {},
                       "product-is": {},
                       "product-ei": {"WSO2_CARBON_DB_CORE": ['dbscripts/oracle.sql'],
                                      "WSO2_MB_STORE_DB": ['wso2/broker/dbscripts/mb-store/oracle-mb.sql'],
                                      "BPS_DS": ['wso2/business-process/dbscripts/bps/bpel/create/oracle.sql'],
                                      "ACTIVITI_DB": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.oracle.create.identity.sql'],
                                      "WSO2_METRICS_DB": ['wso2/broker/dbscripts/metrics/oracle.sql']}}},

    "POSTGRESQL": {"prefix": "jdbc:postgresql://", "driverClassName": "org.postgresql.Driver",
                   "jarName": "postgres.jar",
                   "DB_SETUP": {"product-apim": {},
                                "product-is": {},
                                "product-ei": {"WSO2_CARBON_DB_CORE": ['dbscripts/postgresql.sql'],
                                               "BPS_DS": ['wso2/business-process/dbscripts/bps/bpel/create/postgresql.sql'],
                                               "ACTIVITI_DB": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.postgres.create.identity.sql']}}
                   }}
