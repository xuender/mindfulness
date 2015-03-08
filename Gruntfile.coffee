module.exports = (grunt)->
  grunt.loadNpmTasks('grunt-contrib-clean')
  grunt.loadNpmTasks('grunt-contrib-uglify')
  grunt.loadNpmTasks('grunt-contrib-watch')
  grunt.loadNpmTasks('grunt-contrib-copy')
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
      dist: ['bin', 'pkg', 'public']
    bump:
      options:
        part: 'patch'
      files: ['package.json', 'bower.json']
    copy:
      angular:
        files: [
          cwd: 'bower_components/angular/'
          src: [
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
      angularI18n:
        files: [
          cwd: 'bower_components/angular-i18n/'
          src: [
            'angular-locale_zh-cn.js'
          ]
          dest: 'public/js'
          expand: true
          filter: 'isFile'
        ]
      angular_route:
        files: [
          cwd: 'bower_components/angular-route/'
          src: [
            'angular-route.js'
            'angular-route.min.js'
            'angular-route.min.js.map'
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
      fontCss:
        files: [
          cwd: 'bower_components/font-awesome/css'
          src: [
            'font-awesome.min.css'
          ]
          dest: 'public/css'
          expand: true
          filter: 'isFile'
        ]
      font:
        files: [
          cwd: 'bower_components/font-awesome/fonts'
          src: [
            '*'
          ]
          dest: 'public/fonts'
          expand: true
          filter: 'isFile'
        ]
    coffee:
      options:
        bare: true
      chapter:
        files:
          'public/js/note.min.js': [
            'src/note/note.coffee'
          ]
          'public/js/web.min.js': [
            'src/web/web.coffee'
          ]
    uglify:
      main:
        files:
          'bin/js/note.min.js': [
            'bin/js/note.min.js'
          ]
    htmlmin:
      dist:
        options:
          removeComments: true,
          collapseWhitespace: true
        files:
          'public/note.html': 'src/note/note.html'
    cssmin:
      web:
        expand: true
        cwd: 'src/web/'
        src: ['*.css', '!*.min.css'],
        dest: 'public/css/',
        ext: '.min.css'
    watch:
      css:
        files: [
          'src/**/*.css'
        ]
        tasks: ['cssmin']
      html:
        files: [
          'src/**/*.html'
        ]
        tasks: ['htmlmin']
      coffee:
        files: [
          'src/**/*.coffee'
        ]
        tasks: ['coffee']
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
    #'uglify'
  ])
  grunt.registerTask('deploy', [
    'bump'
    'dist'
  ])
  grunt.registerTask('travis', 'travis test', ['karma:travis'])
  grunt.registerTask('default', ['dist'])
