###
bookCtrl.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
BookCtrl = ($scope, $http, $log, ngTableParams, $filter, $q)->
  $scope.$parent.name = 'book'
  $log.debug 'xxx %s'
  $scope.b =
    title: ''
  $scope.ok = ->
    $http.post('/note/book', $scope.b).success((data)->
      if data.ok
        $log.debug data
      else
        alert(data.err)
    )
  #$scope.tableParams = new ngTableParams(
  #  page: 1
  #  count: 10
  #  sorting:
  #    read: 'asc'
  #    ca: 'desc'
  #,
  #  getData: ($defer, params)->
  #    # 过滤
  #    $http.post('/note/books',
  #      Page: params.page()
  #      Count: params.count()
  #      Sorting: params.orderBy()
  #      Filter: params.filter()
  #    ).success((data)->
  #      $log.debug data
  #      params.total(data.count)
  #      $defer.resolve(data.data)
  #    )
  #)
  $scope.read = (d)->
    # 读取
    if !d.read
      $http.get("/post/#{d.id}").success((data)->
        $log.debug data
        if data.ok
          d.read=true
        else
          alert(data.err)
      )
    d.$edit=!d.$edit

BookCtrl.$inject = [
  '$scope'
  '$http'
  '$log'
  'ngTableParams'
  '$filter'
  '$q'
]
