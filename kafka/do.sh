#!/bin/sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TF_STATE_DIR=$DIR
export TF_STATE=${TF_STATE:-"$TF_STATE_DIR/terraform.tfstate"}
if [[ ! -f "$TF_STATE" ]];
then
    pushd $TF_STATE_DIR
    terraform show -json > terraform.tfstate
    popd
fi
/usr/local/bin/terraform-inventory $@ 1> /dev/stdout 2> /dev/null

