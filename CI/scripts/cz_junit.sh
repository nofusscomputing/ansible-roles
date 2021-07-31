#!/bin/bash

# to use ensure cz_exit=0 is set prior to the cz command so that if the command is successfull, this script works

cz_command=$(cat cz_outut.log)


if [ "f${cz_exit}" == "f" ]; then
echo "environmental variable cz_exit must be set"
#exit 2
fi

if [ "${cz_exit}" == "0" ]; then
error_count=0
system_err=''
else
error_count=1
system_err="ERROR: $cz_command"

fi

#echo boo;

#echo "output:[$cz_command]"
echo "[DEBUG] cz_exit[$cz_exit]"


cat <<EOF
<testsuites id="conventional commits" name="CI Validation test" tests="1" failures="$error_count" time="0">
    <testsuite id="conventional commit" name="testing" tests="1" failures="$error_count" time="0">
        <testcase classname="Conventional Commits" file="https://www.conventionalcommits.org/en/v1.0.0/" line="0" name="Using Conventional Commits" time="0" timestamp="$(date '+%Y-%m-%d %H:%M:%S')">
            <system-out>
                <![CDATA[ $cz_command ]]>
            </system-out>
            <system-err>
                <![CDATA[ $system_err ]]>
            </system-err>
        </testcase>
    </testsuite>
</testsuites>

EOF

#exit $command_exit
