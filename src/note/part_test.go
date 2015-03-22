package note

import (
	. "github.com/smartystreets/goconvey/convey"
	"gopkg.in/mgo.v2/bson"
	"testing"
)

func TestPart(t *testing.T) {
	Convey("段落创建", t, func() {
		p := Part{
			Section: bson.NewObjectId(),
		}
		Convey("拆分元素", func() {
			p.SetSpan("弟子规，圣人讯。首孝悌，次谨信。")
			So(len(p.Span), ShouldEqual, 4)
			So(p.Span[0], ShouldEqual, "弟子规，")
			So(p.Span[2], ShouldEqual, "首孝悌，")
		})
	})
}
