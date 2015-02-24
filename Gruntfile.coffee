module.exports = (grunt)->
  grunt.loadNpmTasks('grunt-contrib-clean')
  grunt.loadNpmTasks('grunt-contrib-uglify')
  grunt.loadNpmTasks('grunt-contrib-watch')
  grunt.loadNpmTasks('grunt-contrib-copy')
  grunt.loadNpmTasks('grunt-karma')
  grunt.loadNpmTasks('grunt-contrib-coffee')
  grunt.loadNpmTasks('grunt-coffeelint')
  grunt.loadNpmTasks('grunt-contrib-cssmin')
  grunt.loadNpmTasks('grunt-contrib-htmlmin')
  grunt.loadNpmTasks('grunt-shell')
  grunt.loadNpmTasks('grunt-bumpx')

  grunt.initConfig(
    pkg:
      grunt.file.readJSON('package.json')
    clean:
      dist: ['dist']
    bump:
      options:
        part: 'patch'
      files: ['package.json', 'bower.json']
    copy:
      angular:
        files: [
          cwd: 'bower_components/angular/'
          src: [
            'angular.js'
            'angular.min.js'
            'angular.min.js.map'
          ]
          dest: 'public/js'
          expand: true
          filter: 'isFile'
        ]
      angularBootstrap:
        files: [
          cwd: 'bower_components/angular-bootstrap/'
          src: [
            'ui-bootstrap-tpls.min.js'
          ]
          dest: 'public/js'
          expand: true
          filter: 'isFile'
        ]
      jquery:
        files: [
          cwd: 'bower_components/jquery/'
          src: [
            'jquery.min.js'
            'jquery.min.map'
          ]
          dest: 'public/js'
          expand: true
          filter: 'isFile'
        ]
      bootstrap:
        files: [
          cwd: 'bower_components/bootstrap/dist/'
          src: [
            'css/bootstrap.min.css'
            'js/bootstrap.min.js'
            'fonts/*'
          ]
          dest: 'public'
          expand: true
          filter: 'isFile'
        ]
    coffee:
      options:
        bare: true
      chapter:
        files:
          'public/js/web.min.js': [
            'js/web.coffee'
          ]
    uglify:
      main:
        files:
          'dist/js/web.min.js': [
            'public/js/web.min.js'
          ]
    htmlmin:
      dist:
        options:
          removeComments: true,
          collapseWhitespace: true
        files:
          'public/demo.html': 'demo.html'
    cssmin:
      toolbox:
        expand: true
        cwd: 'css/'
        src: ['*.css', '!*.min.css'],
        dest: 'public/css/',
        ext: '.min.css'
    watch:
      css:
        files: [
          'css/*.css'
        ]
        tasks: ['cssmin']
      html:
        files: [
          '*.html'
        ]
        tasks: ['htmlmin']
      coffee:
        files: [
          'js/*.coffee'
        ]
        tasks: ['coffee']
    compress:
      google:
        options:
          archive: 'dist/toolbox.zip'
        files: [
          {expand: true, cwd: 'dist', src: '**/*', dest: '/'}
        ]
    karma:
      options:
        configFile: 'karma.conf.js'
      dev:
        colors: true,
      travis:
        singleRun: true
        autoWatch: false
  )
  grunt.registerTask('test', ['karma'])
  grunt.registerTask('dev', [
    'clean'
    'copy',
    'htmlmin'
    'cssmin'
    'coffee'
  ])
  grunt.registerTask('dist', [
    'dev'
    'uglify'
    'compress'
  ])
  grunt.registerTask('deploy', [
    'bump'
    'dist'
  ])
  grunt.registerTask('travis', 'travis test', ['karma:travis'])
  grunt.registerTask('default', ['dist'])
