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
WSO2SERVER='bin/integrator.sh'
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
M2_PATH = {"product-is": "is/wso2is",
           "product-apim": "am/wso2am",
           "product-ei": "ei/wso2ei"}
DIST_POM_PATH = {"product-is": "modules/distribution/pom.xml",
                 "product-apim": "modules/distribution/product/pom.xml",
                 "product-ei": "distribution/pom.xml"}
LIB_PATH = {"product-apim": "",
            "product-is": "",
            "product-ei": "lib"}
DISTRIBUTION_PATH = {"product-apim": "modules/distribution/product/target",
                     "product-is": "modules/distribution/target",
                     "product-ei": "distribution/target"}
INTEGRATION_PATH = {"product-apim": "modules/integration",
                    "product-is": "modules/integration",
                    "product-ei": "integration"}
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
TEST_OUTPUT_DIR_NAME = "test_outputs"
ARTIFACT_REPORTS_PATHS = {"product-apim": [],
                  "product-is": [],
                  "product-ei": {"mediation-tests-service": ["integration/mediation-tests/tests-service/target/surefire-reports",
                                                             "integration/mediation-tests/tests-service/target/logs/automation.log"],
                                 "mediation-tests-transport": ["integration/mediation-tests/tests-transport/target/surefire-reports",
                                                                "integration/mediation-tests/tests-transport/target/logs/automation.log"],
                                 "mediation-tests-mediator-1": ["integration/mediation-tests/tests-mediator-1/target/surefire-reports",
                                                                "integration/mediation-tests/tests-mediator-1/target/logs/automation.log"],
                                 "mediation-tests-mediator-2": ["integration/mediation-tests/tests-mediator-2/target/surefire-reports",
                                                                "integration/mediation-tests/tests-mediator-2/target/logs/automation.log"],
                                 "mediation-tests-patches": ["integration/mediation-tests/tests-patches/target/surefire-reports",
                                                             "integration/mediation-tests/tests-patches/target/logs/automation.log"],
                                 "mediation-tests-other": ["integration/mediation-tests/tests-other/target/surefire-reports",
                                                           "integration/mediation-tests/tests-other/target/logs/automation.log"],
                                 "business-process-bpel": ["integration/business-process-tests/tests-integration/bpel/target/surefire-reports",
                                                           "integration/business-process-tests/tests-integration/bpel/target/logs/automation.log"],
                                 "business-process-bpmn": ["integration/business-process-tests/tests-integration/bpmn/target/surefire-reports",
                                                           "integration/business-process-tests/tests-integration/bpmn/target/logs/automation.log"],
                                 "business-process-humantasks": ["integration/business-process-tests/tests-integration/humantasks/target/surefire-reports",
                                                                 "integration/business-process-tests/tests-integration/humantasks/target/logs/automation.log"],
                                 "business-process-taskcoordination": ["integration/business-process-tests/tests-integration/taskcoordination/target/surefire-reports",
                                                                       "integration/business-process-tests/tests-integration/taskcoordination/target/logs/automation.log"],
                                 "dataservice-hosting-integration-tests": ["integration/dataservice-hosting-tests/tests-integration/tests/target/surefire-reports",
                                                                           "integration/dataservice-hosting-tests/tests-integration/tests/target/logs/automation.log"],
                                 "business-process-patches-bpel": ["integration/business-process-tests/tests-patches/bpel/target/surefire-reports"]
                               }
                  }
IGNORE_DIR_TYPES = {"product-apim": [],
                     "product-is": [],
                     "product-ei": ["ESBTestSuite","junitreports","BPS Test Suite","bps-server-startup","BPS HumanTask TestSuite","BPS HumanTask Coordination TestSuite","DssTestSuite"]
                    }
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
                                 "ACTIVITI_DB_BPS": [
                                     'wso2/business-process/dbscripts/bps/bpmn/create/activiti.mysql.create.identity.sql']
                                 }}},

    "SQLSERVER-SE": {"prefix": "jdbc:sqlserver://",
                     "driverClassName": "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jarName": "sqlserver-ex.jar",
                     "DB_SETUP": {
                         "product-apim": {},
                         "product-is": {},
                         "product-ei": {"WSO2_CARBON_DB_CORE": ['dbscripts/mssql.sql'],
                                        "WSO2_CARBON_DB_BROKER": ['wso2/broker/dbscripts/mssql.sql'],
                                        "WSO2_CARBON_DB_BPS": ['wso2/business-process/dbscripts/mssql.sql'],
                                        "WSO2_MB_STORE_DB_BROKER": ['wso2/broker/dbscripts/mb-store/mssql-mb.sql'],
                                        "WSO2_METRICS_DB_BROKER": ['wso2/broker/dbscripts/metrics/mssql.sql'],
                                        "BPS_DS_BPS": ['wso2/business-process/dbscripts/bps/bpel/create/mssql.sql'],
                                        "ACTIVITI_DB_BPS": [
                                            'wso2/business-process/dbscripts/bps/bpmn/create/activiti.mssql.create.identity.sql']}}},

    "ORACLE-SE2": {"prefix": "jdbc:oracle:thin:@", "driverClassName": "oracle.jdbc.OracleDriver",
                   "jarName": "oracle-se.jar",
                   "DB_SETUP": {
                       "product-apim": {},
                       "product-is": {},
                       "product-ei": {"WSO2_CARBON_DB_CORE": ['dbscripts/oracle.sql'],
                                      "WSO2_CARBON_DB_BROKER": ['wso2/broker/dbscripts/oracle.sql'],
                                      "WSO2_CARBON_DB_BPS": ['wso2/business-process/dbscripts/oracle.sql'],
                                      "WSO2_MB_STORE_DB_BROKER": ['wso2/broker/dbscripts/mb-store/oracle-mb.sql'],
                                      "WSO2_METRICS_DB_BROKER": ['wso2/broker/dbscripts/metrics/oracle.sql'],
                                      "BPS_DS_BPS": ['wso2/business-process/dbscripts/bps/bpel/create/oracle.sql'],
                                      "ACTIVITI_DB_BPS": [
                                          'wso2/business-process/dbscripts/bps/bpmn/create/activiti.oracle.create.identity.sql']}}},

    "POSTGRESQL": {"prefix": "jdbc:postgresql://", "driverClassName": "org.postgresql.Driver",
                   "jarName": "postgres.jar",
                   "DB_SETUP": {"product-apim": {},
                                "product-is": {},
                                "product-ei": {}}
                   }}
