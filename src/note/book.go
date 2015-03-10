package note

import (
	"base"
	"errors"
	"github.com/martini-contrib/render"
	"gopkg.in/mgo.v2/bson"
	"log"
	"time"
	"web"
)

type Book struct {
	Id bson.ObjectId `bson:"_id,omitempty" table:"book"`
	// 标题
	Title string `bson:"title" json:"title"`
	// 作者
	Author string `bson:"author,omitempty" json:"author"`
	//简介
	Summary string `bson:"summary,omitempty" json:"summary"`
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

// 创建帖子
func (b *Book) New() error {
	if b.Id.Valid() {
		return errors.New("ID错误")
	}
	if b.Title == "" {
		return errors.New("标题不能为空")
	}
	return b.Save()
}

// 新增书籍
func BookNew(l web.Log, s web.Session, b Book, r render.Render) {
	log.Printf("book title:%s\n", b.Title)
	ret := web.Msg{}
	err := b.New()
	ret.Ok = err == nil
	if !ret.Ok {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
	l.Log(b.Id, "书籍新增:"+b.Title)
}

// 修改书籍
func BookUpdate(l web.Log, b Book, r render.Render) {
	ret := web.Msg{}
	err := b.Save()
	ret.Ok = err == nil
	if !ret.Ok {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
	l.Log(b.Id, "书籍修改:"+b.Title)
}
