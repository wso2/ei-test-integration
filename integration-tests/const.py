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
DATASOURCE_PATHS = {"product-apim": [],
                    "product-is": [],
                    "product-ei": ["conf/datasources/master-datasources.xml",
                                   "wso2/broker/conf/datasources/master-datasources.xml",
                                   "wso2/broker/conf/datasources/metrics-datasources.xml",
                                   "wso2/business-process/conf/datasources/master-datasources.xml",
                                   "wso2/business-process/conf/datasources/bps-datasources.xml",
                                   "wso2/business-process/conf/datasources/activiti-datasources.xml",
                                   "wso2/analytics/conf/datasources/analytics-datasources.xml",
                                   "wso2/analytics/conf/datasources/master-datasources.xml",
                                   "wso2/analytics/conf/datasources/metrics-datasources.xml",
                                   "wso2/micro-integrator/conf/datasources/master-datasources.xml",
                                   "wso2/msf4j/conf/datasources/metrics-datasources.xml"]}
M2_PATH = {"product-is": "is/wso2is", "product-apim": "am/wso2am",
           "product-ei": "ei/wso2ei"}
DIST_POM_PATH = {"product-is": "modules/distribution/pom.xml", "product-apim": "modules/distribution/product/pom.xml",
                 "product-ei": "distribution/pom.xml"}
LIB_PATH = "repository/lib"
DISTRIBUTION_PATH = {"product-apim": "modules/distribution/product/target",
                     "product-is": "modules/distribution/target",
                     "product-ei": "distribution/target"}
INTEGRATION_PATH = {"product-apim": "modules/api-import-export",
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
LOG_FILE_PATHS = {"product-apim": [],
                  "product-is": [],
                  "product-ei": ["integration/mediation-tests/tests-mediator-1/target/surefire-reports/emailable-report.html",
                                 "integration/mediation-tests/tests-mediator-1/target/surefire-reports/index.html",
                                 "integration/mediation-tests/tests-mediator-1/target/surefire-reports/TEST-TestSuite.xml",
                                 "integration/mediation-tests/tests-mediator-1/target/surefire-reports/testng-results.xml",
                                 "integration/mediation-tests/tests-mediator-1/target/surefire-reports/testng.css",
                                 "integration/mediation-tests/tests-mediator-1/target/surefire-reports/TestSuite.txt",
                                 "integration/mediation-tests/tests-mediator-1/target/logs/automation.log"]}
DB_META_DATA = {
    "MYSQL": {"prefix": "jdbc:mysql://", "driverClassName": "com.mysql.jdbc.Driver", "jarName": "mysql.jar",
              "DB_SETUP": {
                  "product-apim": {},
                  "product-is": {},
                  "product-ei": {"WSO2_CARBON_DB": ['dbscripts/mysql5.7.sql','wso2/broker/dbscripts/mysql5.7.sql',
                                                    'wso2/business-process/dbscripts/mysql5.7.sql','wso2/analytics/dbscripts/mysql5.7.sql',
                                                    'wso2/micro-integrator/dbscripts/mysql5.7.sql'],
                                 "WSO2_MB_STORE_DB": ['wso2/broker/dbscripts/mb-store/mysql-mb.sql'],
                                 "BPS_DS": ['wso2/business-process/dbscripts/bps/bpel/create/mysql.sql'],
                                 "ACTIVITI_DB": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.mysql.create.identity.sql'],
                                 "WSO2_METRICS_DB": ['wso2/broker/dbscripts/metrics/mysql.sql','wso2/analytics/dbscripts/metrics/mysql.sql','wso2/msf4j/dbscripts/metrics/mysql.sql'],
                                 "WSO2_ANALYTICS_EVENT_STORE_DB":[],
                                 "WSO2_ANALYTICS_PROCESSED_DATA_STORE_DB": [],
                                 "WSO2_ANALYTICS_RS_DB_HBASE": [],
                                 "WSO2_ANALYTICS_DS_CASSANDRA": []}}},

    "SQLSERVER-SE": {"prefix": "jdbc:sqlserver://",
                     "driverClassName": "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jarName": "sqlserver-ex.jar",
                     "DB_SETUP": {
                         "product-apim": {},
                         "product-is": {},
                         "product-ei": {"WSO2_CARBON_DB": ['dbscripts/mssql.sql','wso2/broker/dbscripts/mssql.sql',
                                                           'wso2/business-process/dbscripts/mssql.sql','wso2/analytics/dbscripts/mssql.sql',
                                                           'wso2/micro-integrator/dbscripts/mssql.sql'],
                                        "WSO2_MB_STORE_DB": ['wso2/broker/dbscripts/mb-store/mssql-mb.sql'],
                                        "BPS_DS": ['wso2/business-process/dbscripts/bps/bpel/create/mssql.sql'],
                                        "ACTIVITI_DB": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.mssql.create.identity.sql'],
                                        "WSO2_METRICS_DB": ['wso2/broker/dbscripts/metrics/mssql.sql','wso2/analytics/dbscripts/metrics/mssql.sql','wso2/msf4j/dbscripts/metrics/mysql.sql'],
                                        "WSO2_ANALYTICS_EVENT_STORE_DB": [],
                                        "WSO2_ANALYTICS_PROCESSED_DATA_STORE_DB": [],
                                        "WSO2_ANALYTICS_RS_DB_HBASE": [],
                                        "WSO2_ANALYTICS_DS_CASSANDRA": []
                                        }}},

    "ORACLE-SE2": {"prefix": "jdbc:oracle:thin:@", "driverClassName": "oracle.jdbc.OracleDriver",
                   "jarName": "oracle-se.jar",
                   "DB_SETUP": {
                       "product-apim": {},
                       "product-is": {},
                       "product-ei": {"WSO2_CARBON_DB": ['dbscripts/oracle.sql','wso2/broker/dbscripts/oracle.sql',
                                                         'wso2/business-process/dbscripts/oracle.sql','wso2/analytics/dbscripts/oracle.sql',
                                                         'wso2/micro-integrator/dbscripts/oracle.sql'],
                                      "WSO2_MB_STORE_DB": ['wso2/broker/dbscripts/mb-store/oracle-mb.sql'],
                                      "BPS_DS": ['wso2/business-process/dbscripts/bps/bpel/create/oracle.sql'],
                                      "ACTIVITI_DB": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.oracle.create.identity.sql'],
                                      "WSO2_METRICS_DB": ['wso2/broker/dbscripts/metrics/oracle.sql','wso2/analytics/dbscripts/metrics/oracle.sql','wso2/msf4j/dbscripts/metrics/mysql.sql'],
                                      "WSO2_ANALYTICS_EVENT_STORE_DB": [],
                                      "WSO2_ANALYTICS_PROCESSED_DATA_STORE_DB": [],
                                      "WSO2_ANALYTICS_RS_DB_HBASE": [],
                                      "WSO2_ANALYTICS_DS_CASSANDRA": []
                                      }}},

    "POSTGRESQL": {"prefix": "jdbc:postgresql://", "driverClassName": "org.postgresql.Driver",
                   "jarName": "postgres.jar",
                   "DB_SETUP": {"product-apim": {},
                                "product-is": {},
                                "product-ei": {"WSO2_CARBON_DB": ['dbscripts/postgresql.sql','wso2/broker/dbscripts/postgresql.sql',
                                                                  'wso2/business-process/dbscripts/postgresql.sql','wso2/analytics/dbscripts/postgresql.sql',
                                                                  'wso2/micro-integrator/dbscripts/postgresql.sql'],
                                               "WSO2_MB_STORE_DB": ['wso2/broker/dbscripts/mb-store/postgresql-mb.sql'],
                                               "BPS_DS": ['wso2/business-process/dbscripts/bps/bpel/create/postgresql.sql'],
                                               "ACTIVITI_DB": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.postgres.create.identity.sql'],
                                               "WSO2_METRICS_DB": ['wso2/broker/dbscripts/metrics/postgresql.sql','wso2/analytics/dbscripts/metrics/postgresql.sql','wso2/msf4j/dbscripts/metrics/postgresql.sql'],
                                               "WSO2_ANALYTICS_EVENT_STORE_DB": [],
                                               "WSO2_ANALYTICS_PROCESSED_DATA_STORE_DB": [],
                                               "WSO2_ANALYTICS_RS_DB_HBASE": [],
                                               "WSO2_ANALYTICS_DS_CASSANDRA": []
                                               }}
                   }}
