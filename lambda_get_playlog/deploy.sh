#!/bin/bash
# My first script

echo "Creating deployment package"

mkdir deploy

echo "Copying src files"
cp -r src/* deploy

echo "Copying virtualenv (/env) files"
cp -r env/* deploy

echo "zipping"
cd deploy
zip -r ../deploy.zip .
cd ..

echo "cleaning up"
rm -rf deploy
 
echo "done"

