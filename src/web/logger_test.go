package web

import (
	"base"
	. "github.com/smartystreets/goconvey/convey"
	"gopkg.in/mgo.v2/bson"
	"testing"
)

// 日志查询
//func TestLogQuery(t *testing.T) {
//	base.DbTest()
//	defer base.DbClose()
//	Convey("日志查询 log.Query", t, func() {
//		uid := bson.NewObjectId()
//		n := Log{
//			Uid:  uid,
//			Work: "测试",
//		}
//		n.New()
//		n = Log{
//			Uid:  uid,
//			Work: "测试",
//		}
//		n.New()
//		Convey("缺少条件", func() {
//			l := Log{}
//			p := base.Params{
//				Page:  1,
//				Count: 100,
//			}
//			_, _, err := l.Query(p)
//			So(err, ShouldNotBeNil)
//		})
//		Convey("查询成功", func() {
//			l := Log{}
//			l.Uid = uid
//			p := base.Params{
//				Page:  1,
//				Count: 100,
//			}
//			ls, count, err := l.Query(p)
//			So(err, ShouldBeNil)
//			So(len(ls), ShouldEqual, 2)
//			So(count, ShouldEqual, 2)
//			Convey("2页", func() {
//				p.Page = 2
//				p.Count = 1
//				ls, count, err = l.Query(p)
//				So(count, ShouldEqual, 2)
//				So(len(ls), ShouldEqual, 1)
//			})
//			Convey("1页", func() {
//				p.Page = 1
//				p.Count = 1
//				ls, count, err = l.Query(p)
//				So(count, ShouldEqual, 2)
//				So(len(ls), ShouldEqual, 1)
//			})
//		})
//	})
//}

// 日志创建
func TestLogNew(t *testing.T) {
	base.DbTest()
	defer base.DbClose()
	Convey("日志新建 log.New", t, func() {
		uid := bson.NewObjectId()
		Convey("错误", func() {
			n := Log{
				Uid:  uid,
				Work: "测试",
			}
			So(n.New(), ShouldBeNil)
			So(n.Uid, ShouldEqual, uid)
			So(n.New(), ShouldNotBeNil)
		})
		Convey("内容错误", func() {
			n := Log{
				Uid: uid,
			}
			So(n.New(), ShouldNotBeNil)
		})
		Convey("用户错误", func() {
			n := Log{
				Work: "xxx",
			}
			So(n.New(), ShouldNotBeNil)
		})
	})
}
