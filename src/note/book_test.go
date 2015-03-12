package note

import (
	"base"
	. "github.com/smartystreets/goconvey/convey"
	"testing"
)

func TestBook(t *testing.T) {
	base.DbTest()
	defer base.DbClose()
	Convey("书籍测试", t, func() {
		b := Book{
			Title: "测试",
		}
		b.New()
		//Convey("Top 头12条", func() {
		//	bs := BookTop()
		//	So(len(bs), ShouldEqual, 1)
		//})
	})
}
