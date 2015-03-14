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
	// 书籍查询
	m.Post(p+"/books", web.ManagerJson, binding.Bind(base.Params{}), BookQuery)
	// 获取说有书籍ID对应关系
	m.Get(p+"/books", BookMap)
	// 书籍修改
	m.Put(p+"/book", web.ManagerJson, binding.Bind(Book{}), BookUpdate)
	// 书籍删除
	m.Delete(p+"/book/:id", web.ManagerJson, BookRemove)
	// 书籍增加
	m.Post(p+"/section", web.ManagerJson, binding.Bind(Section{}), SectionNew)
	// 书籍查询
	m.Post(p+"/sections", web.ManagerJson, binding.Bind(base.Params{}), SectionQuery)
	// 书籍修改
	m.Put(p+"/section", web.ManagerJson, binding.Bind(Section{}), SectionUpdate)
	// 书籍删除
	m.Delete(p+"/section/:id", web.ManagerJson, SectionRemove)
}
