package web

import (
	"base"
	. "github.com/smartystreets/goconvey/convey"
	"gopkg.in/mgo.v2/bson"
	"testing"
)

// 日志查询
func TestLogQuery(t *testing.T) {
	base.DbTest()
	defer base.DbClose()
	Convey("日志查询 log.Query", t, func() {
		uid := bson.NewObjectId()
		n := Log{
			Uid:  uid,
			Work: "测试",
		}
		n.New()
		n = Log{
			Uid:  uid,
			Work: "测试",
		}
		n.New()
		Convey("缺少条件", func() {
			l := Log{}
			p := base.Params{
				Page:  1,
				Count: 100,
			}
			_, _, err := l.Query(p)
			So(err, ShouldNotBeNil)
		})
		Convey("查询成功", func() {
			l := Log{}
			l.Uid = uid
			p := base.Params{
				Page:  1,
				Count: 100,
			}
			ls, count, err := l.Query(p)
			So(err, ShouldBeNil)
			So(len(ls), ShouldEqual, 2)
			So(count, ShouldEqual, 2)
			Convey("2页", func() {
				p.Page = 2
				p.Count = 1
				ls, count, err = l.Query(p)
				So(count, ShouldEqual, 2)
				So(len(ls), ShouldEqual, 1)
			})
			Convey("1页", func() {
				p.Page = 1
				p.Count = 1
				ls, count, err = l.Query(p)
				So(count, ShouldEqual, 2)
				So(len(ls), ShouldEqual, 1)
			})
		})
	})
}

// 日志创建
func TestLogNew(t *testing.T) {
	base.DbTest()
	defer base.DbClose()
	uid := bson.NewObjectId()
	n := Log{
		Uid:  uid,
		Work: "测试",
	}
	err := n.New()
	if err != nil {
		t.Errorf("创建日志失败")
	}
	if n.Uid != uid {
		t.Errorf("用户ID错误")
	}
	err = n.New()
	if err == nil {
		t.Errorf("id错误")
	}
	n = Log{
		Uid: uid,
	}
	err = n.New()
	if err == nil {
		t.Errorf("内容不能为空")
	}
	n = Log{
		Work: "xxx",
	}
	err = n.New()
	if err == nil {
		t.Errorf("用户不能为空")
	}
}
