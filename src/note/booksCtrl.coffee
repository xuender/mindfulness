###
bookCtrl.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
BooksCtrl = ($scope, $http, $log, $modal, ngTableParams, $filter, $q)->
  $scope.$parent.name = 'book'
  $scope.new = false
  $log.debug 'xxx'
  $scope.new = ->
    $modal.open(
      templateUrl: 'partials/note/book.html?5.html'
      controller: BookCtrl
      backdrop: 'static'
      size: 'lg'
      resolve:
        book: ->
          title: '未命名'
          author: '无名氏'
          summary: '无'
        del: ->
          false
    ).result.then((b)->
      $http.post('/note/book', b).success((data)->
        if data.ok
          $scope.tableParams.reload()
        else
          alert(data.err)
      )
    ,->
      $log.info '取消'
    )
  $scope.update = (book)->
    $modal.open(
      templateUrl: 'partials/note/book.html?5.html'
      controller: BookCtrl
      backdrop: 'static'
      size: 'lg'
      resolve:
        book: ->
          book
        del: ->
          true
    ).result.then((b)->
      $log.debug b
      if angular.isString(b)
        $http.delete('/note/book/' + b).success((data)->
          if data.ok
            $scope.tableParams.reload()
          else
            alert(data.err)
        )
      else
        $http.put('/note/book', b).success((data)->
          if data.ok
            $scope.tableParams.reload()
          else
            alert(data.err)
        )
    ,->
      $log.info '取消'
    )
  $scope.tableParams = new ngTableParams(
    page: 1
    count: 10
    sorting:
      ca: 'desc'
  ,
    getData: ($defer, params)->
      # 过滤
      $http.post('/note/books',
        Page: params.page()
        Count: params.count()
        Sorting: params.orderBy()
        Filter: params.filter()
      ).success((data)->
        $log.debug data
        params.total(data.count)
        $defer.resolve(data.data)
      )
  )
BooksCtrl.$inject = [
  '$scope'
  '$http'
  '$log'
  '$modal'
  'ngTableParams'
  '$filter'
  '$q'
]
