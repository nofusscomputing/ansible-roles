#!/bin/bash

# to use ensure cz_exit=0 is set prior to the cz command so that if the command is successfull, this script works
# this script must be run with '. {script-name}' so that vars set in cli are available 

cz_command=$(cat cz_output.log)


if [ "f${cz_exit}" == "f" ]; then
echo "[DEBUG] environmental variable cz_exit must be set"
exit 255
fi

if [ "${cz_exit}" == "0" ]; then
error_count=0
system_err=''

cat <<EOF
<testsuite errors="0" name="Conventional Commits Messages Check" tests="0">
    <testcase classname="Conventional Commits" file="CI/commitizen/README.md" name="Using Conventional Commits Message Format"/>
</testsuite>
EOF

else
error_count=1
system_err="ERROR: $cz_command"


cat <<EOF
<testsuites id="Conventional Commits Messages Check" name="CI Validation test" tests="1" errors="$error_count" time="0">
    <testsuite id="conventional commit" name="testing" tests="1" failures="$error_count" time="0">
        <testcase classname="Conventional Commits" file="CI/commitizen/README.md" line="0" name="Using Conventional Commits Message Format" time="0" timestamp="$(date '+%Y-%m-%d %H:%M:%S')">

            <failure message="Conventional commits not used" type="validation">$cz_command
            </failure>
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

fi

#echo boo;

#echo "output:[$cz_command]"
#echo "[DEBUG] cz_exit[$cz_exit]"




exit $cz_exit
