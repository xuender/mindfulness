###
utils.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###

doSpan = (str, row)->
  # 将字符串改造成<span>分割的单词组合
  start = 0
  html = ''
  k = /[\s|，|。]+/
  re = /([\w-]+)|([\s|，|。]+)|(\d+)|([^\x00-\xff])/ig
  r = ''
  while r=re.exec(str)
    #console.info r
    s = r[0]
    if k.test(s)
      html += "<span>#{s}</span>"
    else
      start += 1
      html += "<span id=\"s#{row}_#{start}\">#{s}</span>"
  html

createLine = (x1, y1, x2, y2, color='#000', stroke='1', zindex=1000)->
  # 画线
  isIE = navigator.userAgent.indexOf("MSIE") > -1
  line = document.createElement('div')
  length = Math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
  line.style.width = length + 'px'
  line.style.borderBottom = stroke + 'px solid'
  line.style.borderColor = color
  line.style.position = 'absolute'
  line.style.zIndex = zindex
  if isIE
    line.style.top = (y2 > y1) ? y1 + 'px' : y2 + 'px'
    line.style.left = x1 + 'px'
    nCos = (x2-x1)/length
    nSin = (y2-y1)/length
    line.style.filter = "progid:DXImageTransform.Microsoft.Matrix(sizingMethod='auto expand', M11=" + nCos + ", M12=" + -1*nSin + ", M21=" + nSin + ",M22=" + nCos + ")"
  else
    angle = Math.atan((y2-y1)/(x2-x1))
    line.style.top = y1 + 0.5*length*Math.sin(angle) + 'px'
    line.style.left = x1 - 0.5*length*(1 - Math.cos(angle)) + 'px'
    line.style.MozTransform = line.style.WebkitTransform = line.style.OTransform= 'rotate(' + angle + 'rad)'
  $('body').append(line)

setColor = (s1, s2, color)->
  s1.css('background-color', color)
  if s1.attr('id') != s2.attr('id') and s1.next().attr('id')
      setColor(s1.next(), s2, color)

createAnnotation = (s1, s2, annotation)->
  # 批注连线
  y = s1.offset().top + s1.height() + 3
  x1 = s1.offset().left
  parent = s1.parents('.col-xs-8')
  x2 = parent.offset().left + parent.width()
  bc = annotation.css('background-color')
  setColor(s1, s2, bc)
  createLine(x1, y, x2, y, bc, 2)
  x3 = annotation.offset().left
  y3 = annotation.offset().top + 4
  createLine(x2, y, x3, y3, bc, 2)
