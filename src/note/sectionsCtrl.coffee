###
SectionsCtrl.coffee
Copyright (C) 2014 ender xu <xuender@gmail.com>

Distributed under terms of the MIT license.
###
SectionsCtrl = ($scope, $http, $log, $modal, ngTableParams, $filter, $q)->
  $scope.$parent.name = 'section'
  $scope.books = []
  $scope.selectBooks= ->
    # 书籍列表
    $log.debug 'selectBooks'
    def = $q.defer()
    $http.get('/note/books').success((msg)->
      if msg.ok
        $scope.books = msg.data
        $log.debug $scope.books
        def.resolve($scope.books)
    )
    def
  $scope.bookTitle = (books)->
    angular.forEach(books, (book)->
      angular.forEach($scope.books, (b)->
        if b.id == book.book
          book.bookTitle = b.title
      )
    )
  $scope.new = ->
    $modal.open(
      templateUrl: 'partials/note/section.html?4.html'
      controller: SectionCtrl
      backdrop: 'static'
      size: 'lg'
      resolve:
        section: ->
        del: ->
          false
        books: ->
          $scope.books
    ).result.then((s)->
      $http.post('/note/section', s).success((data)->
        if data.ok
          $scope.tableParams.reload()
        else
          alert(data.err)
      )
    ,->
      $log.info '取消'
    )
  $scope.update = (s)->
    $modal.open(
      templateUrl: 'partials/note/section.html?4.html'
      controller: SectionCtrl
      backdrop: 'static'
      size: 'lg'
      resolve:
        section: ->
          s
        del: ->
          true
        books: ->
          $scope.books
    ).result.then((s)->
      $log.debug s
      if angular.isString(s)
        $http.delete('/note/section/' + s).success((data)->
          if data.ok
            $scope.tableParams.reload()
          else
            alert(data.err)
        )
      else
        $http.put('/note/section', s).success((data)->
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
      book: 'asc'
      order: 'asc'
  ,
    getData: ($defer, params)->
      # 过滤
      $http.post('/note/sections',
        Page: params.page()
        Count: params.count()
        Sorting: params.orderBy()
        Filter: params.filter()
      ).success((data)->
        $log.debug data
        params.total(data.count)
        $scope.bookTitle(data.data)
        $defer.resolve(data.data)
      )
  )
SectionsCtrl.$inject = [
  '$scope'
  '$http'
  '$log'
  '$modal'
  'ngTableParams'
  '$filter'
  '$q'
]
