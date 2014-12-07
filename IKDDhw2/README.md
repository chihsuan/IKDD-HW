Homework 2
=======

## Run

    python IKDDhw2.py [query-string]

## Description

<p>Given a query string (either in English or Chinese) as the input, connect to iservDB and retrieve twitter data containing the query string. Finally print out every matching text ,its user_id, user_name (defined in iservDB) and sort according to the user ID in the ascendant order. Please show the result in the table form as the following example, and print the table out in console</p>

Implement a Java / python program.

iservDB:

    host: iservdb.cloudopenlab.org.tw          port: 5432

Arguments:

    1. query: Specify the keyword for query. For example: 王建民

Running Examples:

    Input: 王建民

    Output: text user_name user_id
