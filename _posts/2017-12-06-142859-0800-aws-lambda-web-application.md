---
layout: default
date: 2017-12-06 14:28:59 -0800
title: aws lambda web application
---

Issues I encountered

* the lambda function must return a valid API response and in the header section it must have a "Access-Control-Allow-Origin" value.
* In Cognito, it appears that you cannot use the email address as the username exactly, but you can replace "@" with "-at-" for the username.
* needed to allow connection from any IP in mongodb atlas

