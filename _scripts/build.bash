#!/bin/bash
jekyll build
cd _site
git add --all
git commit -m 'build site'
git push origin master

