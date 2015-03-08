package web

import (
	. "github.com/smartystreets/goconvey/convey"
	"testing"
)

// 页面新建
func TestPageNew(t *testing.T) {
	Convey("新建页面 Page", t, func() {
		Convey("命名", func() {
      p := PageNew("test", false)
			So(p.Title, ShouldEqual, "test - ")
    })
		Convey("没有命名", func() {
      p := PageNew("", false)
			So(p.Title, ShouldEqual, "")
    })
  })
}
