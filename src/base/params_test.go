package base

import (
	. "github.com/smartystreets/goconvey/convey"
	"testing"
)

func TestParams(t *testing.T) {
	Convey("分页 Params", t, func() {
		p := Params{
			Page:  3,
			Count: 100,
		}
		Convey("起始 Skip", func() {
			So(p.Skip(), ShouldEqual, 200)
		})
		Convey("限制 Limit", func() {
			So(p.Limit(), ShouldEqual, 100)
		})
		Convey("排序 Sort", func() {
			So(p.Sort("def"), ShouldEqual, "def")
			p.Sorting = []string{"ca"}
			So(p.Sort("def"), ShouldEqual, "ca")
		})
	})
}
