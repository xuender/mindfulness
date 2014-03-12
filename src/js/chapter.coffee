###
chapter.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###

$ ->
  # test
  createAnnotation($('#s1'), $('#s1'), $('#a1'))
  createAnnotation($('#s2'), $('#s3'), $('#a2'))
  createAnnotation($('#s4'), $('#s5'), $('#a3'))

angular.module('book', [
  'ui.bootstrap'
]).directive('context', ->
  # <p context>内容</p> 转换 
  # <p><span id="s1_1">内</span><span id="s1_2">容</span></p>
  ($scope, elm, attr)->
    html = ''
    row = 0
    for p in elm.text().split('\n')
      row += 1
      html += '<p>'
      html += doSpan(p, row)
      html += '</p>'
    elm.html(html)
).directive('line', ->
  #TODO <line row="1" start="4" end="5" to="1"/> 画第1行4到5个字到第一个批注连线
  ($scope, elm, attr)->
    1
)

BookCtrl = ($scope)->
  $scope.as = [
    {
      row: 1
      start: 3
      end: 3
      context: '规则'
    }
    {
      row: 1
      start: 4
      end: 5
      context: '孔子'
    }
  ]
  console.info $scope.as
BookCtrl.$inject = ['$scope']
