package base

import (
	. "github.com/smartystreets/goconvey/convey"
	"gopkg.in/mgo.v2/bson"
	"testing"
	"time"
)

type TestObj struct {
	Id bson.ObjectId `bson:"_id,omitempty" json:"id" table:"to"`
	// 标题
	Title string `bson:"title" json:"title"`
	// 名称
	Name string `bson:"name" json:"name"`
	// 测试ID
	Tid bson.ObjectId `bson:"tid,omitempty" json:"tid"`
	// 创建时间
	Ca time.Time `bson:"ca,omitempty" json:"ca"`
	// 创建时间
	Ua time.Time `bson:"ua,omitempty" json:"ua"`
}
type TestObj2 struct {
	Id bson.ObjectId `bson:"_id,omitempty" json:"id" table:"to2"`
	// 标题
	Title string `bson:"title" json:"title"`
	// 创建时间
	Ca time.Time `bson:"ca,omitempty" json:"ca"`
	// 创建时间
	Ua time.Time `bson:"ua,omitempty" json:"ua"`
	// 删除时间
	Ra time.Time `bson:"ra,omitempty" json:"ra"`
}

// 保存
func TestSave(t *testing.T) {
	DbTest()
	defer DbClose()
	o := TestObj{
		Title: "123",
	}
	Save(&o)
	if !o.Id.Valid() {
		t.Errorf("主键错误")
	}
}

// 查找
func TestFind(t *testing.T) {
	DbTest()
	defer DbClose()
	o := TestObj{
		Title: "123",
	}
	Save(&o)
	n := TestObj{
		Id: o.Id,
	}
	Find(&n)
	if n.Title != "123" {
		t.Errorf("查找错误")
	}
}

// 查找M
func TestFindM(t *testing.T) {
	DbTest()
	defer DbClose()
	o := TestObj{
		Title: "123",
	}
	Save(&o)
	n := TestObj{}
	m := make(map[string]interface{})
	m["title"] = "123"
	FindM(&n, m)
	if n.Title != "123" {
		t.Errorf("查找错误")
	}
}

// count
func TestCount(t *testing.T) {
	DbTest()
	defer DbClose()
	o := TestObj{
		Title: "123",
	}
	Save(&o)
	n := TestObj{}
	m := bson.M{
		"title": "123",
	}
	c := Count(&n, m)
	if c != 1 {
		t.Errorf("统计错误")
	}
}

// 删除
func TestRemove(t *testing.T) {
	DbTest()
	defer DbClose()
	o := TestObj{
		Title: "123",
	}
	Save(&o)
	err := Remove(&o)
	if err != nil {
		t.Errorf("删除错误")
	}
}

// 删除2
func TestRemove2(t *testing.T) {
	DbTest()
	defer DbClose()
	o := TestObj2{
		Title: "123",
	}
	Save(&o)
	err := Remove(&o)
	if err != nil {
		t.Errorf("删除错误")
	}
	n := TestObj2{
		Id: o.Id,
	}
	Find(&n)
	if n.Title != "123" {
		t.Errorf("虚拟删除错误")
	}
}
func TestQuery(t *testing.T) {
	DbTest()
	defer DbClose()
	Convey("数据排序 Query", t, func() {
		o := TestObj{
			Title: "123",
			Name:  "1",
		}
		Save(&o)
		o1 := TestObj{
			Title: "123",
			Name:  "2",
		}
		Save(&o1)
		tid := bson.NewObjectId()
		o2 := TestObj{
			Title: "1",
			Name:  "3",
			Tid:   tid,
		}
		Save(&o2)
		Convey("查询", func() {
			var r []TestObj
			m := bson.M{
				"title": "123",
			}
			Convey("排序", func() {
				Query(&o, &r, m)
				So(len(r), ShouldEqual, 2)
			})
			Convey("排序 name", func() {
				Query(&o, &r, m, "name")
				So(r[0].Name, ShouldEqual, "1")
			})
			Convey("排序 -name", func() {
				Query(&o, &r, m, "-name")
				So(r[0].Name, ShouldEqual, "2")
			})
		})
		Convey("查询ID", func() {
			var r []TestObj
			m := bson.M{
				"tid": tid.Hex(),
			}
			Query(&o, &r, m)
			So(len(r), ShouldEqual, 1)
		})
		Convey("查询ObjectId", func() {
			var r []TestObj
			m := bson.M{
				"tid": tid,
			}
			Query(&o, &r, m)
			So(len(r), ShouldEqual, 1)
		})
	})
}
