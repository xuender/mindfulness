package main

import (
	"base"
	"github.com/go-martini/martini"
	"github.com/martini-contrib/render"
	"github.com/martini-contrib/sessions"
	"log"
	"note"
	"web"
)

func main() {
	//base.LogInit("/tmp/a.log")
	base.LogDev()
	log.Println("网站启动...")
	defer log.Println("网站关闭.")
	log.Println("连接数据库.")
	base.DbOpen("127.0.0.1", "note")
	defer base.DbClose()
	log.Println("启动WEB服务.")
	m := martini.Classic()
	m.Use(render.Renderer(render.Options{
		Layout: "layout",
		Delims: render.Delims{"{[{", "}]}"},
	}))
	store := sessions.NewCookieStore([]byte("xuender@gmail.com"))
	m.Use(sessions.Sessions("f_session", store))
	// 客户网址
	web.Path(m, "/")
	// 客服网址
	web.CsPath(m, "/cs")
	// 注解网址
	note.Path(m, "/note")
	m.NotFound(func(r render.Render) {
		r.HTML(404, "404", nil)
	})
	// 端口号
	//http.ListenAndServe(":3000", m)
	m.Run()
}
