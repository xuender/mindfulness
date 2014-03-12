###
commandSpec.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
describe 'doSpan', ->
  it 'span', ->
    expect(doSpan(' ', 1)).toEqual('<span> </span>')
    expect(doSpan('\t ', 1)).toEqual('<span>\t </span>')
    expect(doSpan('我 book书', 1)).toEqual('<span id="s1_1">我</span><span> </span><span id="s1_2">book</span><span id="s1_3">书</span>')
