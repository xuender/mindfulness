package note

import (
	"base"
	. "github.com/smartystreets/goconvey/convey"
	"gopkg.in/mgo.v2/bson"
	"testing"
)

//func TestSection(t *testing.T) {
//	base.DbTest()
//	defer base.DbClose()
//	Convey("章节", t, func() {
//		b := Book{
//			Title: "测试",
//		}
//		b.New()
//		Convey("新建错误", func() {
//			s := Section{}
//			Convey("标题错误", func() {
//				s.Book = b.Id
//				So(s.New(), ShouldNotBeNil)
//			})
//			Convey("书籍错误", func() {
//				s.Title = "title"
//				So(s.New(), ShouldNotBeNil)
//			})
//			Convey("内容错误", func() {
//				s.Title = "title"
//				s.Book = b.Id
//				So(s.New(), ShouldNotBeNil)
//			})
//			Convey("没有错误", func() {
//				s.Title = "title"
//				s.Book = b.Id
//        s.Content = "xxx"
//				So(s.New(), ShouldBeNil)
//			})
//		})
//		Convey("序号", func() {
//			s := Section{}
//			s.Title = "title"
//			s.Book = b.Id
//      s.Content = "xxx"
//			s.New()
//			Convey("新增", func() {
//				So(s.Order, ShouldEqual, 10)
//			})
//			Convey("新增第二个", func() {
//				s2 := Section{}
//				s2.Title = "title2"
//				s2.Book = b.Id
//        s2.Content = "xxx"
//				s2.New()
//				So(s.Order, ShouldEqual, 10)
//				So(s2.Order, ShouldEqual, 20)
//				Convey("新增第三个", func() {
//					s3 := Section{}
//					s3.Title = "title3"
//					s3.Book = b.Id
//					s3.Order = 15
//          s3.Content = "xxx"
//					s3.New()
//					s2.Find()
//					So(s.Order, ShouldEqual, 10)
//					So(s3.Order, ShouldEqual, 20)
//					So(s2.Order, ShouldEqual, 30)
//					Convey("移动位置", func() {
//						s2.Order = 3
//						s2.Update()
//						s3.Find()
//						s.Find()
//						So(s2.Order, ShouldEqual, 10)
//						So(s.Order, ShouldEqual, 20)
//						So(s3.Order, ShouldEqual, 30)
//					})
//				})
//			})
//		})
//	})
//}
func TestCreatePart(t *testing.T) {
	base.DbTest()
	defer base.DbClose()
	Convey("章节创建", t, func() {
		s := Section{}
		s.Title = "title"
		s.Book = bson.NewObjectId()
		Convey("内容为空", func() {
			So(s.CreateParts(), ShouldNotBeNil)
			s.Content = " "
			So(s.CreateParts(), ShouldNotBeNil)
		})
	})
}
