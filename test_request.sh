#!/usr/bin/env sh

# curl -X POST -H "Content-type: application/json" -d '{"seed":"hoge"}' http://wp.ymizushi.info/session
curl -X POST -H "Content-type: application/json" -d '{"input":"定義これは1です"}' http://wp.ymizushi.info/session/10/eval
curl -X POST -H "Content-type: application/json" -d '{"input":"これを評価"}' http://wp.ymizushi.info/session/10/eval
curl -X POST -H "Content-type: application/json" -d '{"input":"1+1"}' http://wp.ymizushi.info/session/10/eval

curl -X POST -H "Content-type: application/json" -d '{"input":"定義それは1です"}' http://wp.ymizushi.info/session/10/eval
curl -X POST -H "Content-type: application/json" -d '{"input":"それを評価"}' http://wp.ymizushi.info/session/10/eval
curl -X POST -H "Content-type: application/json" -d '{"input":"3+3"}' http://wp.ymizushi.info/session/10/eval
