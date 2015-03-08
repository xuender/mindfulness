package main

import (
	"github.com/go-martini/martini"
	"github.com/martini-contrib/render"
	"github.com/martini-contrib/sessions"
	"log"
	"web"
)

func main() {
	log.Println("网站启动...")
	defer log.Println("网站关闭.")
	//TODO 链接数据库
	m := martini.Classic()
	m.Use(render.Renderer(render.Options{
		Layout: "layout",
		Delims: render.Delims{"{[{", "}]}"},
	}))
	store := sessions.NewCookieStore([]byte("xuender@gmail.com"))
	m.Use(sessions.Sessions("f_session", store))
	// 客户网址
	web.Path(m, "/")
	m.NotFound(func(r render.Render) {
		r.HTML(404, "404", nil)
	})
	// 端口号
	//http.ListenAndServe(":3000", m)
	m.Run()
}
