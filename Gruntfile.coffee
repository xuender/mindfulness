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
      #d3:
      #  files: [
      #    cwd: 'bower_components/d3/'
      #    src: [
      #      'd3.min.js'
      #    ]
      #    dest: 'web/static/js'
      #    expand: true
      #    filter: 'isFile'
      #  ]
      angular:
        files: [
          cwd: 'bower_components/angular/'
          src: [
            'angular.js'
            'angular.min.js'
            'angular.min.js.map'
          ]
          dest: 'web/static/js'
          expand: true
          filter: 'isFile'
        ]
      angularBootstrap:
        files: [
          cwd: 'bower_components/angular-bootstrap/'
          src: [
            'ui-bootstrap-tpls.min.js'
          ]
          dest: 'web/static/js'
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
          dest: 'web/static/js'
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
          dest: 'web/static'
          expand: true
          filter: 'isFile'
        ]
    coffee:
      options:
        bare: true
      chapter:
        files:
          'web/static/js/chapter.min.js': [
            'src/js/utils.coffee'
            'src/js/chapter.coffee'
            'src/js/web.coffee'
          ]
    uglify:
      main:
        files:
          'dist/js/main.min.js': [
            'dist/js/main.min.js'
          ]
      background:
        files:
          'dist/js/background.js': [
            'dist/js/background.js'
          ]
    htmlmin:
      dist:
        options:
          removeComments: true,
          collapseWhitespace: true
        files: {}
        #  'web/static/annotation.html': 'src/annotation.html'
    cssmin:
      toolbox:
        expand: true
        cwd: 'src/css/'
        src: ['*.css', '!*.min.css'],
        dest: 'web/static/css/',
        ext: '.min.css'
    shell:
      runServer:
        command: 'web/manage.py runserver --insecure'
        options:
          stdout: true
          stdin: true
          stderr: true
    watch:
      css:
        files: [
          'src/**/*.css'
        ]
        tasks: ['cssmin']
      html:
        files: [
          'src/*.html'
        ]
        tasks: ['htmlmin']
      coffee:
        files: [
          'src/**/*.coffee'
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
