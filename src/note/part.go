package note

import (
	"base"
	"errors"
	"gopkg.in/mgo.v2/bson"
	"time"
)

// 段落
type Part struct {
	Id bson.ObjectId `bson:"_id,omitempty" json:"id" table:"part"`
	// 章节
	Section bson.ObjectId `bson:"section" json:"section"`
	// 元素
	Span []string `bson:"span" json:"span"`
	// 顺序
	Order int `bson:"order" json:"order"`
	// 创建时间
	Ca time.Time `bson:"ca,omitempty" json:"ca"`
	// 修改时间
	Ua time.Time `bson:"ua,omitempty" json:"ua"`
}

// 保存
func (o *Part) Save() error {
	return base.Save(o)
}

// 查找
func (o *Part) Find() error {
	return base.Find(o)
}

// 删除
func (o *Part) Remove() error {
	return base.Remove(o)
}

// 创建
func (o *Part) New() error {
	if o.Id.Valid() {
		return errors.New("ID错误")
	}
	if len(o.Span) == 0 {
		return errors.New("元素不能为空")
	}
	return o.Update()
}

// 修改
func (o *Part) Update() error {
	m := bson.M{
		"section": o.Section,
	}
	parts := []Part{}
	err := base.Query(o, &parts, m, "order")
	if err != nil {
		return err
	}
	if len(parts) == 0 {
		o.Order = 10
	} else {
		order := 0
		u := true
		for _, os := range parts {
			if os.Id == o.Id {
				continue
			}
			order += 10
			if o.Order > (order-10) && o.Order <= order {
				o.Order = order
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
		if o.Order != order {
			if o.Order == 0 || u {
				o.Order = order
			}
		}
	}
	return o.Save()
}

// 设置span
func (o *Part) SetSpan(str string) {
	o.Span = base.SplitAfter(str, []string{"，", "。"})
}
