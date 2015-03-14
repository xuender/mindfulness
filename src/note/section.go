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

// 章节
type Section struct {
	Id bson.ObjectId `bson:"_id,omitempty" json:"id" table:"section"`
	// 书籍
	Book bson.ObjectId `bson:"book" json:"book"`
	// 标题
	Title string `bson:"title" json:"title"`
	// 顺序
	Order int `bson:"order" json:"order"`
	// 内容
	Content string `bson:"content,omitempty" json:"content"`
	// 创建时间
	Ca time.Time `bson:"ca,omitempty" json:"ca"`
	// 修改时间
	Ua time.Time `bson:"ua,omitempty" json:"ua"`
}

// 保存
func (s *Section) Save() error {
	return base.Save(s)
}

// 查找
func (s *Section) Find() error {
	return base.Find(s)
}

// 删除
func (s *Section) Remove() error {
	return base.Remove(s)
}

// 创建
func (s *Section) New() error {
	if s.Id.Valid() {
		return errors.New("ID错误")
	}
	if s.Title == "" {
		return errors.New("标题不能为空")
	}
	if !s.Book.Valid() {
		return errors.New("所属书籍不能为空")
	}
	return s.Update()
}

// 修改
func (s *Section) Update() error {
	m := bson.M{
		"book": s.Book,
	}
	sections := []Section{}
	err := base.Query(s, &sections, m, "order")
	if err != nil {
		return err
	}
	if len(sections) == 0 {
		s.Order = 10
	} else {
		order := 0
		u := true
		for _, os := range sections {
			if os.Id == s.Id {
				continue
			}
			order += 10
			if s.Order > (order-10) && s.Order <= order {
				s.Order = order
				order += 10
				u = false
			}
			if os.Order != order {
				os.Order = order
				os.Save()
			}
		}
		order += 10
		//log.Printf("%d, %d\n", s.Order, order)
		if s.Order != order {
			if s.Order == 0 || u {
				s.Order = order
			}
		}
	}
	return s.Save()
}

// 查询
func (s *Section) Query(p base.Params) (sections []Section, count int, err error) {
	m := bson.M{}
	count, err = p.QueryM(s, "order", &sections, m)
	return
}

// 章节新增
func SectionNew(l web.Log, s web.Session, e Section, r render.Render) {
	log.Printf("章节新增 title:%s\n", e.Title)
	ret := web.Msg{}
	err := e.New()
	ret.Ok = err == nil
	if !ret.Ok {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
	l.Log(e.Id, "章节新增:"+e.Title)
}

// 章节修改
func SectionUpdate(l web.Log, s Section, r render.Render) {
	log.Printf("章节修改 title:%s\n", s.Title)
	ret := web.Msg{}
	err := s.Update()
	ret.Ok = err == nil
	if !ret.Ok {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
	l.Log(s.Id, "章节修改:"+s.Title)
}

// 章节查询
func SectionQuery(params base.Params, r render.Render) {
	s := Section{}
	ret := web.Msg{}
	ls, count, err := s.Query(params)
	log.Printf("章节查询 params:%s, count:%d\n", params, count)
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
func SectionRemove(l web.Log, params martini.Params, r render.Render) {
	s := Section{
		Id: bson.ObjectIdHex(params["id"]),
	}
	err := s.Find()
	if err == nil {
		err = s.Remove()
		l.Log(s.Id, "章节删除:"+s.Title)
	}
	ret := web.Msg{}
	ret.Ok = err == nil
	if !ret.Ok {
		ret.Err = err.Error()
	}
	r.JSON(200, ret)
}
