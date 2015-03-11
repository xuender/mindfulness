package note

import (
	"base"
	"github.com/go-martini/martini"
	"github.com/martini-contrib/binding"
	"github.com/martini-contrib/render"
	"web"
)

// 注释网址
func Path(m *martini.ClassicMartini, p string) {
	m.Get(p, func(r render.Render) {
		r.HTML(200, "note", web.PageNew("书籍管理", true))
	})
	// 书籍增加
	m.Post(p+"/book", web.ManagerJson, binding.Bind(Book{}), BookNew)
	// 查询用户反馈列表
	m.Post(p+"/books", web.ManagerJson, binding.Bind(base.Params{}), BookQuery)
	// 书籍修改
	m.Put(p+"/book", web.ManagerJson, binding.Bind(Book{}), BookUpdate)
	// 书籍删除
	m.Delete(p+"/book/:id", web.ManagerJson, BookRemove)
}
