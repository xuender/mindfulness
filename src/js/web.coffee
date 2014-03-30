###
web.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###

USER_IDS = []
showLine = ->
  $('.line').remove()
  $('.ann').each(->
    a = JSON.parse($(this).attr('data'))
    if a.user in USER_IDS
      css = 'user' + USER_IDS.indexOf(a.user)
    else
      css = 'userMe'
    createAnnotation(
      $("#s#{a.row}_#{a.start}"),
      $("#s#{a.row}_#{a.end}"),
      $("#a#{a.id}"),
      css
    )
  )
$ ->
  $('.ann').onPositionChanged(->
    showLine()
  )
  showLine()
  # 显示所有下划线
  showUnderLine()
showUnderLine = ->
  $('.sul').each(->
    a = JSON.parse($(this).attr('data'))
    underline(
      $("#s#{a.row}_#{a.start}"),
      $("#s#{a.row}_#{a.end}"),
      ["ul_#{a.style}", 'userMe']
    )
  )


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
