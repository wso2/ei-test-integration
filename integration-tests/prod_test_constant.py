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


INTEGRATOR = "bin/integrator"
ANALYTICS = "wso2/analytics/wso2/worker/bin/carbon"
BROKER = "wso2/broker/bin/wso2server"
BP = "wso2/business-process/bin/wso2server"
MICRO_INTG = "wso2/micro-integrator/bin/wso2server"
DATASOURCE_PATHS = {"CORE": ["conf/datasources/master-datasources.xml"],
                    "BROKER": ["wso2/broker/conf/datasources/master-datasources.xml",
                               "wso2/broker/conf/datasources/metrics-datasources.xml"],
                    "BPS": ["wso2/business-process/conf/datasources/master-datasources.xml",
                            "wso2/business-process/conf/datasources/bps-datasources.xml",
                            "wso2/business-process/conf/datasources/activiti-datasources.xml"]
                    }
M2_PATH = "ei/wso2ei"
DIST_POM_PATH = "distribution/pom.xml"
LIB_PATH = "lib"
DISTRIBUTION_PATH = "distribution/target"
INTEGRATION_PATH = "integration/mediation-tests/tests-mediator-1"
POM_FILE_PATHS = {}

# Add testng files to be replaced. E.g "integration/mediation-tests/tests-mediator-1/src/test/resources/testng.xml"
TESTNG_DIST_XML_PATHS = {"integration/business-process-tests/pom.xml",
                         "integration/business-process-tests/tests-integration/bpel/src/test/resources/testng-server-mgt.xml",
                         "integration/business-process-tests/tests-integration/bpel/src/test/resources/testng.xml",
                         "integration/business-process-tests/tests-integration/bpmn/src/test/resources/testng.xml",
                         "integration/business-process-tests/tests-integration/humantasks/src/test/resources/testng.xml",
                         "integration/business-process-tests/tests-integration/pom.xml",
                         "integration/mediation-tests/pom.xml",
                         "integration/mediation-tests/tests-mediator-2/src/test/resources/testng.xml",
                         "integration/mediation-tests/tests-patches/src/test/resources/testng.xml",
                         "integration/mediation-tests/tests-service/src/test/resources/testng.xml",
                         "integration/mediation-tests/tests-transport/src/test/resources/testng.xml",
                         "integration/pom.xml"}

ARTIFACT_REPORTS_PATHS = {"mediation-tests-mediator-1": ["integration/mediation-tests/tests-mediator-1/target/surefire-reports",
                                                         "integration/mediation-tests/tests-mediator-1/target/logs/automation.log"]
                          }
IGNORE_DIR_TYPES = {"ESBTestSuite",
                    "junitreports",
                    "BPS Test Suite",
                    "bps-server-startup",
                    "BPS HumanTask TestSuite",
                    "BPS HumanTask Coordination TestSuite",
                    "DssTestSuite"}
DB_META_DATA = {
    "MYSQL": {"prefix": "jdbc:mysql://", "driverClassName": "com.mysql.jdbc.Driver", "jarName": "mysql.jar",
              "DB_SETUP": {"WSO2_CARBON_DB_CORE": ['dbscripts/mysql5.7.sql'],
                           "WSO2_CARBON_DB_BROKER": ['wso2/broker/dbscripts/mysql5.7.sql'],
                           "WSO2_CARBON_DB_BPS": ['wso2/business-process/dbscripts/mysql5.7.sql'],
                           "WSO2_MB_STORE_DB_BROKER": ['wso2/broker/dbscripts/mb-store/mysql-mb.sql'],
                           "WSO2_METRICS_DB_BROKER": ['wso2/broker/dbscripts/metrics/mysql.sql'],
                           "BPS_DS_BPS": ['wso2/business-process/dbscripts/bps/bpel/create/mysql.sql'],
                           "ACTIVITI_DB_BPS": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.mysql.create.engine.sql',
                                               'wso2/business-process/dbscripts/bps/bpmn/create/activiti.mysql.create.history.sql',
                                               'wso2/business-process/dbscripts/bps/bpmn/create/activiti.mysql.create.identity.sql',
                                               'wso2/business-process/dbscripts/bps/bpmn/create/activiti.mysql.create.substitute.sql']
                           }
              },
    "SQLSERVER-SE": {"prefix": "jdbc:sqlserver://",
                     "driverClassName": "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jarName": "sqlserver-ex.jar",
                     "DB_SETUP": {"WSO2_CARBON_DB_CORE": ['dbscripts/mssql.sql'],
                                  "WSO2_CARBON_DB_BROKER": ['wso2/broker/dbscripts/mssql.sql'],
                                  "WSO2_CARBON_DB_BPS": ['wso2/business-process/dbscripts/mssql.sql'],
                                  "WSO2_MB_STORE_DB_BROKER": ['wso2/broker/dbscripts/mb-store/mssql-mb.sql'],
                                  "WSO2_METRICS_DB_BROKER": ['wso2/broker/dbscripts/metrics/mssql.sql'],
                                  "BPS_DS_BPS": ['wso2/business-process/dbscripts/bps/bpel/create/mssql.sql'],
                                  "ACTIVITI_DB_BPS": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.mssql.create.engine.sql',
                                                      'wso2/business-process/dbscripts/bps/bpmn/create/activiti.mssql.create.history.sql',
                                                      'wso2/business-process/dbscripts/bps/bpmn/create/activiti.mssql.create.identity.sql',
                                                      'wso2/business-process/dbscripts/bps/bpmn/create/activiti.mssql.create.substitute.sql']
                                  }
                     },

    "ORACLE-SE2": {"prefix": "jdbc:oracle:thin:@", "driverClassName": "oracle.jdbc.OracleDriver",
                   "jarName": "oracle-se.jar",
                   "DB_SETUP": {"WSO2_CARBON_DB_CORE": ['dbscripts/oracle.sql'],
                                "WSO2_CARBON_DB_BROKER": ['wso2/broker/dbscripts/oracle.sql'],
                                "WSO2_CARBON_DB_BPS": ['wso2/business-process/dbscripts/oracle.sql'],
                                "WSO2_MB_STORE_DB_BROKER": ['wso2/broker/dbscripts/mb-store/oracle-mb.sql'],
                                "WSO2_METRICS_DB_BROKER": ['wso2/broker/dbscripts/metrics/oracle.sql'],
                                "BPS_DS_BPS": ['wso2/business-process/dbscripts/bps/bpel/create/oracle.sql'],
                                "ACTIVITI_DB_BPS": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.oracle.create.engine.sql',
                                                    'wso2/business-process/dbscripts/bps/bpmn/create/activiti.oracle.create.history.sql',
                                                    'wso2/business-process/dbscripts/bps/bpmn/create/activiti.oracle.create.identity.sql',
                                                    'wso2/business-process/dbscripts/bps/bpmn/create/activiti.oracle.create.substitute.sql']
                                }
                   },

    "POSTGRESQL": {"prefix": "jdbc:postgresql://", "driverClassName": "org.postgresql.Driver",
                   "jarName": "postgres.jar",
                   "DB_SETUP": {"WSO2_CARBON_DB_CORE": ['dbscripts/postgres.sql'],
                                "WSO2_CARBON_DB_BROKER": ['wso2/broker/dbscripts/postgres.sql'],
                                "WSO2_CARBON_DB_BPS": ['wso2/business-process/dbscripts/postgres.sql'],
                                "WSO2_MB_STORE_DB_BROKER": ['wso2/broker/dbscripts/mb-store/postgres-mb.sql'],
                                "WSO2_METRICS_DB_BROKER": ['wso2/broker/dbscripts/metrics/postgres.sql'],
                                "BPS_DS_BPS": ['wso2/business-process/dbscripts/bps/bpel/create/postgres.sql'],
                                "ACTIVITI_DB_BPS": ['wso2/business-process/dbscripts/bps/bpmn/create/activiti.postgres.create.engine.sql',
                                                    'wso2/business-process/dbscripts/bps/bpmn/create/activiti.postgres.create.history.sql',
                                                    'wso2/business-process/dbscripts/bps/bpmn/create/activiti.postgres.create.identity.sql',
                                                    'wso2/business-process/dbscripts/bps/bpmn/create/activiti.postgres.create.substitute.sql']
                                }
                   }
}
