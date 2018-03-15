#!/bin/bash

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


esbHost=$esbHost
esbPort=$esbPort
bpsHost=$bpsHost
bpsPort=$bpsPort
mbHost-$mbHost
mbPort-$mbPort
analyticsHost=$analyticsHost
analyticsPort=$analyticsPort

prgdir=$(dirname "$0")
scriptPath=$(cd "$prgdir"; pwd)

#updating jmeter properties - user.properties
sed -i "s|^\(esbHost\s*=\s*\).*\$|\1${esbHost}|" $scriptPath/../resources/user.properties
sed -i "s|^\(esbPort\s*=\s*\).*\$|\1${esbPort}|" $scriptPath/../resources/user.properties
sed -i "s|^\(bpsHost\s*=\s*\).*\$|\1${bpsHost}|" $scriptPath/../resources/user.properties
sed -i "s|^\(bpsPort\s*=\s*\).*\$|\1${bpsPort}|" $scriptPath/../resources/user.properties
sed -i "s|^\(mbHost\s*=\s*\).*\$|\1${mbHost}|" $scriptPath/../resources/user.properties
sed -i "s|^\(mbPort\s*=\s*\).*\$|\1${mbPort}|" $scriptPath/../resources/user.properties
sed -i "s|^\(analyticsHost\s*=\s*\).*\$|\1${analyticsHost}|" $scriptPath/../resources/user.properties
sed -i "s|^\(analyticsPort\s*=\s*\).*\$|\1${analyticsPort}|" $scriptPath/../resources/user.properties

source $scriptPath/../base-setup.sh > $scriptPath/basesetup.log
