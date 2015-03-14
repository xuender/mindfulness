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
		Convey("新建状态", func() {
			b := Book{
				Title: "测试",
			}
			b.New()
			So(b.Status, ShouldEqual, "new")
		})
	})
}
