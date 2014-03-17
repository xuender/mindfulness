###
utils.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###

selectData = ->
  #获取选择的位置信息
  ret = {}
  s = window.getSelection()
  if s.type == 'Range'
    base = $(s.anchorNode.parentNode)
    extent = $(s.extentNode.parentNode)
    b = true
    while b
      id = base.attr('id')
      if id and id.length > 3
        ids = id.substring(1).split('_')
        ret['end'] = ids[1]
        ret['row'] = ids[0]
        if 'start' not of ret
          ret['start'] = ids[1]
      b = base.size() > 0 and base[0] != extent[0]
      base = base.next()
    ret

jQuery.fn.onPositionChanged = (trigger, millis)->
  #位置变化事件
  if (millis == null)
    millis = 100
  o = $(this[0])
  if (o.length < 1)
    return o

  lastPos = null
  lastOff = null
  setInterval(->
    if o == null or o.length < 1
      return o
    if lastPos == null
      lastPos = o.position()
    if lastOff == null
      lastOff = o.offset()
    newPos = o.position()
    newOff = o.offset()
    if lastPos.top != newPos.top or lastPos.left != newPos.left
      $(this).trigger('onPositionChanged',
        lastPos: lastPos
        newPos: newPos
      )
      if typeof (trigger) == "function"
        trigger(lastPos, newPos)
      lastPos = o.position()
    if lastOff.top != newOff.top or lastOff.left != newOff.left
      $(this).trigger('onOffsetChanged',
        lastOff: lastOff
        newOff: newOff
      )
      if typeof (trigger) == "function"
        trigger(lastOff, newOff)
      lastOff= o.offset()
  , millis)
  o

doSpan = (str, row)->
  # 将字符串改造成<span>分割的单词组合，思考一下是否有必要放到后台执行
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
  line.classList.add('line')
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
  # 设置颜色区域
  s1.css('background-color', color)
  if s1.attr('id') != s2.attr('id') and s1.next().attr('id')
      setColor(s1.next(), s2, color)

underline = (s1, s2, style, start=null)->
  # 给对象s1到s2之间所有对象画线
  y1 = s1.offset().top + s1.height() + 3
  x1 = s1.offset().left
  y2 = s2.offset().top + s2.height() + 3
  x2 = s2.offset().left + s2.width()
  if y1 == y2
    createLine(x1, y1, x2, y2, 'red', 2)
    if start !=null && s1[0] != start[0]
      underline(start, s1.prev(), style, start)
  else
    if start == null
      start = s1
    underline(s1.next(), s2, style, start)

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
