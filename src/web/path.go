package web

import (
	"github.com/go-martini/martini"
	//"github.com/martini-contrib/binding"
	"github.com/martini-contrib/render"
)

// 网址设置
func Path(m *martini.ClassicMartini, p string) {
	// 首页
	m.Get(p, func(r render.Render) {
		r.HTML(200, "index", PageNew("", false))
	})
}
