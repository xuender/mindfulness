package note

import (
	"base"
	"errors"
	"github.com/go-martini/martini"
	"github.com/martini-contrib/render"
	"gopkg.in/mgo.v2/bson"
	"log"
	"time"
	"web"
)

const (
	发布 = "publish"
	编辑 = "edit"
	新建 = "new"
)

// 书籍
type Book struct {
	Id bson.ObjectId `bson:"_id,omitempty" json:"id" table:"book"`
	// 标题
	Title string `bson:"title" json:"title"`
	// 作者
	Author string `bson:"author,omitempty" json:"author"`
	//简介
	Summary string `bson:"summary,omitempty" json:"summary"`
	// 状态
	Status string `bson:"status,omitempty" json:"status"`
	// 注释数量
	Size rune `bson:"size,omitempty" json:"size"`
	// 创建时间
	Ca time.Time `bson:"ca,omitempty" json:"ca"`
	// 修改时间
	Ua time.Time `bson:"ua,omitempty" json:"ua"`
}

// 保存
func (b *Book) Save() error {
	return base.Save(b)
}

// 查找
func (p *Book) Find() error {
	return base.Find(p)
}

// 删除
func (p *Book) Remove() error {
	return base.Remove(p)
}

// 创建
func (b *Book) New() error {
	if b.Id.Valid() {
		return errors.New("ID错误")
	}
	if b.Title == "" {
		return errors.New("标题不能为空")
	}
	if b.Status == "" {
		b.Status = 新建
	}
	return b.Save()
}

// 查询
func (b *Book) Query(p base.Params) (books []Book, count int, err error) {
	m := bson.M{}
	count, err = p.QueryM(b, "-ca", &books, m)
	return
}

// 置顶的图书
func BookTop(r render.Render) {
	p := base.Params{
		Page:    1,
		Count:   12,
		Sorting: []string{"-ca"},
		Filter:  map[string]interface{}{"status": 发布},
	}
	b := Book{}
	books, _, _ := b.Query(p)
	homePage := web.PageNew("", false)
	homePage.Data = books
	r.HTML(200, "index", homePage)
}

// 书籍新增
func BookNew(l web.Log, s web.Session, b Book, r render.Render) {
	log.Printf("书籍新增 title:%s\n", b.Title)
	ret := web.Msg{}
	err := b.New()
	ret.Ok = err == nil
	if !ret.Ok {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
	l.Log(b.Id, "书籍新增:"+b.Title)
}

// 书籍修改
func BookUpdate(l web.Log, b Book, r render.Render) {
	log.Printf("书籍修改 title:%s\n", b.Title)
	ret := web.Msg{}
	err := b.Save()
	ret.Ok = err == nil
	if !ret.Ok {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
	l.Log(b.Id, "书籍修改:"+b.Title)
}

// 所有书籍列表
func BookMap(r render.Render) {
	b := Book{}
	ret := web.Msg{}
	p := base.Params{
		Page:    1,
		Count:   100,
		Sorting: []string{"-ca"},
	}
	ls, count, err := b.Query(p)
	m := make(map[string]string)
	if err == nil && count > 0 {
		for _, i := range ls {
			m[i.Id.Hex()] = i.Title
		}
	}
	ret.Ok = err == nil
	if ret.Ok {
		ret.Data = base.Selecter4Map(m)
	} else {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
}

// 书籍查询
func BookQuery(params base.Params, r render.Render) {
	b := Book{}
	ret := web.Msg{}
	ls, count, err := b.Query(params)
	log.Printf("书籍查询 params:%s, count:%d\n", params, count)
	ret.Ok = err == nil
	if err == nil {
		ret.Count = count
		ret.Data = ls
	} else {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
}

// 书籍删除
func BookRemove(l web.Log, params martini.Params, r render.Render) {
	b := Book{
		Id: bson.ObjectIdHex(params["id"]),
	}
	err := b.Find()
	if err == nil {
		err = b.Remove()
		l.Log(b.Id, "书籍删除:"+b.Title)
	}
	ret := web.Msg{}
	ret.Ok = err == nil
	if !ret.Ok {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
}
