###
web.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###

showLine = ->
  $('.line').remove()
  $('.ann').each(->
    a = JSON.parse($(this).attr('data'))
    createAnnotation(
      $("#s#{a.row}_#{a.start}"),
      $("#s#{a.row}_#{a.end}"),
      $("#a#{a.id}")
    )
  )
$ ->
  $('.ann').onPositionChanged(->
    showLine()
  )
  showLine()

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
)
