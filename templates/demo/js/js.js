$(document).ready(function(){ // JQuery运行
// ++++++++++ 定义 ++++++++++
    // ------ 命名 ------
    var M_TOP = 'mob_top', // 窄屏 div 顶部按钮
        HEADER = 'header', // div 顶部
        CONTENT = 'content', // div 正文
        SIDEBAR_FIXED = 'sidebar-fixed', // div 侧边栏 跟随滚动
        CONTENT_NAV_TIP = 'contentNavTip', // 侧边跟随提示的目录 外框
        CONTENT_NAV_TIP_UL = 'table-of-contents', // 侧边跟随提示的目录 列表
        DRUG_SEARCH_BOOK = 'searchBooks' // 药材栏目 书籍关联项目 列表
        ;
    // ------ 固定值 ------
    var $isIE6=!-[1,]&&!window.XMLHttpRequest,
        $HEADER = $('#'+HEADER),
        $CONTENT = $('#'+CONTENT),
            $CONTENT_TOP = $CONTENT.offset().top,
        $SIDEBAR_FIXED = $('#'+SIDEBAR_FIXED),
        $SIDEBAR_FIXED_TOP = $SIDEBAR_FIXED.offset().top,
            $CONTENT_NAV_TIP = $('#'+CONTENT_NAV_TIP),
                $CONTENT_NAV_TIP_UL = $('#'+CONTENT_NAV_TIP_UL),
                $CONTENT_HI = $CONTENT_NAV_TIP_UL.length ? $CONTENT.children('[id^="hi-"]') : false, // 存在侧边跟随提示目录，取正文标题集合
            $DRUG_SEARCH_BOOK = $('#'+DRUG_SEARCH_BOOK)
        ;
    // ------ 变动值 ------
    var $WIN = $(window),
        // $WIN_SMALL = screen.availWidth<=768?true:false, // 屏幕
        $WIN_SMALL = window.innerWidth<=768?true:false, // 浏览器
        $WIN_SCRO_TOP = $WIN.scrollTop()+4
        ;

// ++++++++++ 事件 ++++++++++
    _Static();_Fixed();// 开始
    $(window).on('scroll resize load', function(){_Fixed();});// 窗口移动 下拉 完全加载

    function _Static(){
        A_Login();// 登陆
        A_Logout();// 退出
        A_Sidebar_Small();// 边栏目录高度
        B_Sidebar_Tip_NoScroll();// 当前位置 初始状态的确定
        A_WebInfo();// 页面底部
        A_PopBigImg();
        A_TuShu_Page();
        B_Keydown_Page();
        B_AD_Right();
        // baidu 分享
        window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"","bdPic":"","bdStyle":"0","bdSize":($WIN_SMALL?'32':'16')},"share":{}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];
    }
    function _Fixed(){
        $WIN_SMALL = window.innerWidth<=768?true:false; // 浏览器
        $WIN_SCRO_TOP = $WIN.scrollTop()+4;
        M_TopDiv();// 移动端顶部栏
        M_AD_Fixed_Footer();// 移动屏幕，底部广告
        M_ContentNavTip_Drug();// 药材页面内导航
        B_Sidebar_Fixed();// 监听滚动 边栏定位
        B_Sidebar_Tip_IsScroll();// 当前位置 监听滚动
    }

// ++++++++++ 窄屏 函数 ++++++++++
    // 药材页面内导航
    function M_ContentNavTip_Drug (){
        var i = $('#contentNavTip.drug');
        if(!i.length){return;}
        if( $WIN_SMALL ){
            $CONTENT_NAV_TIP_UL.insertAfter('#'+CONTENT+' h1').css({'max-height':200,'overflow':'auto','overflow-x':'hidden'});
            i.hide();
        }else{
            i.show();
            $CONTENT_NAV_TIP_UL.insertAfter('#'+CONTENT_NAV_TIP+' h2').removeAttr('style');
        }
    }

    // 广告 悬浮页面最下方
    function M_AD_Fixed_Footer (){
        var i = $('#ad_fixed_footer');
        if(i.length){return;}
        if( $WIN_SMALL ){
            var t = '<div id="ad_fixed_footer">';
                t += '<a href="http://m.jgsf.cn/" target="_blank">专业中医文化设计</a>';
                t += '<a href="http://tb.cn/pFBGdkw" target="_blank">中医古籍</a>';
                t += '<a href="http://tb.cn/AojkMkw" target="_blank">针灸铜人</a>';
                t += '<a href="http://tb.cn/KcPowuw" target="_blank">中医展品</a>';
                t += '<a href="http://tb.cn/ffG7qlw" target="_blank">中医字画</a>';
                t += '<a href="http://m.jgsf.cn" target="_blank">中医馆设计</a>';
                t += '</div>';
            $HEADER.after(t);
        }else{
            i.remove();
        }
    }

    // 移动端 添加顶部栏
    function M_TopDiv(){
        var divTop = $('#'+M_TOP);
        if($WIN_SMALL && divTop.length<=0){
            // 添加
            var t = '<div id="'+M_TOP+'">';
                    t += '<a onclick="JavaScript:history.back(-1);" title="返回" class="icon24 i-left" href="javascript:void(0)"></a>';
                    t += '<a data-login="login" data-title="第三方登陆" class="icon24 i-login" href="javascript:void(0)"></a>';
                    t += '<a data-click="bdsearch" title="搜索" class="icon24 i-search" href="javascript:void(0)"></a>';
                    t += '<a data-click="bdsharebuttonbox" title="分享" class="icon24 i-share" href="javascript:void(0)"></a>';
                    if($CONTENT_NAV_TIP.length>0){ t += '<a data-pop="'+CONTENT_NAV_TIP+'" class="icon24 i-article" href="javascript:void(0)"></a>'; }
                    if($DRUG_SEARCH_BOOK.length>0){ t += '<a data-pop="'+DRUG_SEARCH_BOOK+'" class="icon24 i-book" href="javascript:void(0)"></a>'; }
                t += '</div>';
            $HEADER.append(t);
            // pop 菜单
            $('[data-pop]').on('click', function(){
                var s = $(this).attr('data-pop'),
                    n = $( '#' + s ),
                    t = n.children('h2').text(),
                    v = s==CONTENT_NAV_TIP&&n.hasClass('drug') ? $CONTENT_NAV_TIP_UL : n.children('ul') ;
                layer.open({
                    type: 1,
                    title: t,
                    content: v,
                    shadeClose: true,
                    area:['95%','80%']
                });
            });
            // pop 点击
            $('[data-click]').on('click', function(et){
                var n = $( '#' + $(this).attr('data-click') );
                layer.open({
                    type: 1,
                    title: $(this).attr('title'),
                    shadeClose: true,
                    area:['95%','50%'],
                    // skin: 'layui-layer-rim', //加上边框
                    content: n
                });
            });
            return;
        }
        else if(!$WIN_SMALL && divTop.length>0){
            divTop.remove();
            $('[data-pop]').off('click');
            $('[data-click]').off('click');
            return;
        }
    }

// ++++++++++ 宽屏 函数 ++++++++++
    // 监听滚动 边栏定位
    function B_Sidebar_Fixed(){
        if($WIN_SMALL||!$SIDEBAR_FIXED.length){return;}
        if($WIN_SMALL&&$SIDEBAR_FIXED.length){$SIDEBAR_FIXED.hasClass('top').removeAttr('style');return;}// fixed的边栏复位。

        var cH = $CONTENT.outerHeight(),
            cM = cH + $CONTENT_TOP,
            sH = $SIDEBAR_FIXED.outerHeight(),
            fE = cM - sH;
        if( cH < sH || cM < $WIN.height() || $WIN_SCRO_TOP < $SIDEBAR_FIXED_TOP) { $SIDEBAR_FIXED.removeAttr('style'); return; }
        else {
            cssPos = $isIE6 ? 'absolute' : 'fixed';
            if( $WIN_SCRO_TOP>=$SIDEBAR_FIXED_TOP && $WIN_SCRO_TOP < fE ){
                if($SIDEBAR_FIXED.css('top') > 0){return false;}
                cssTop = $isIE6 ? $WIN_SCRO_TOP : 4;
            }else{
                cssPos = 'absolute'; cssTop = fE-$SIDEBAR_FIXED_TOP;
            }
            $SIDEBAR_FIXED.css({'position':cssPos,'top':cssTop });
        }
    };

    // --------- 边栏目录 的跟随提示 ---------
        function B_Sidebar_Tip_NoScroll(){ // 初始状态的确定
            if(!$CONTENT_NAV_TIP.length||!$CONTENT_NAV_TIP_UL.length){ return; }
            var i = $CONTENT_NAV_TIP_UL.find('[data-hi="'+ $CONTENT_HI.first().attr('id') +'"]');// 查找边栏目录对应项li
            if( i.attr('data-cc')>1 ){ i.children('ul').attr('style','background-color:#FFF8C7;');}// li下有ul，设置区块背景
            B_Sidebar_Tip_CssStartTop(i);
        };
        function B_Sidebar_Tip_IsScroll(){ // 移动时 边栏目录 的跟随提示
            if($WIN_SMALL||!$CONTENT_NAV_TIP.length||$CONTENT_NAV_TIP_UL.length<=0||$WIN_SCRO_TOP<$SIDEBAR_FIXED_TOP){ return; }

            var now,t=false;
            $CONTENT_HI.each(function(){
                var f = $(this);
                if(f.offset().top-60 <= $WIN_SCRO_TOP){ t=f.attr('id'); }
                else{ return false; }
            }); // alert(now);
            if(!t){ return; }
            now = $CONTENT_NAV_TIP_UL.find('[data-hi="'+t+'"]');
            B_Sidebar_Tip_CssStartTop(now);
        };
        function B_Sidebar_Tip_CssStartTop(n){ // 增加样式
            $CONTENT_NAV_TIP_UL.scrollTop( n.offset().top - $CONTENT_NAV_TIP_UL.offset().top + $CONTENT_NAV_TIP_UL.scrollTop() - 30 );//定位
            var a = n.children('a');
            if( a.attr('data-tip-now') == 'now' ){ return false; }
            $CONTENT_NAV_TIP_UL.find('a[data-tip-now]').removeAttr('data-tip-now style');
            a.css({'color':'white','background-color':'#FF6633','padding':'1px 2px'}).attr('data-tip-now','now');//当前a
        }

    // --------- 键盘左右键翻页 ---------
    function B_Keydown_Page(){
        if($WIN_SMALL){return;}
        var i=$('#page-nav'); if(!i.length){ return; }
        $(document).on('keydown',function(event){
            var p,char = event.which || event.keyCode;
            if(char===37){ p=i.find('[rel="prev"]').attr('href'); }
            if(char===39){ p=i.find('[rel="next"]').attr('href'); }
            if(p){ window.location.href = p;}
        });
    }

    // --------- 右边栏广告 ---------
    function B_AD_Right(){
        if($WIN_SMALL){return;}
        var i=$('#sidebar-fixed'); if(!i.length){ return; }
        i.append('<div id="my-ad"></div>');// 准备的外层内容
        var ad=$('#my-ad');
        var arr=new Array(// 投放图片编号（数组默认序号）与目标链接
                            'http://jigushanfang.taobao.com/p/rd316515.htm',
                            'http://jigushanfang.taobao.com/p/rd351719.htm',
                            'http://www.jgsf.cn',
                            'http://jigushanfang.taobao.com/p/rd606738.htm',
                            'http://jigushanfang.taobao.com/p/rd049030.htm'
                            );
        var num=new Array(0,1,2,3,4); // 同长度组，用于随机排序
            num.sort(function(){ return 0.5 - Math.random(); }); // 随机随机排序
        var num_c=new Array(0);; // 克隆数组 用于 显示指标
        show_img(); // 页面加载时显示
        setInterval(show_img,3000); // 定时轮播
        function show_img(){// 轮播函数
            if(!num_c.length){ num_c=num.slice(0); } // 重装指标数组
            var arr_n = num_c[0]; // 每次显示的指标（第一个内容）
            ad.empty().append('<a data-n="'+num_c.length+'" href="'+arr[arr_n]+'" target="_blank"><img src="/image/ad/jigushanfang/'+arr_n+'.gif" height="250" width="300"></a>');
            num_c.shift(); // 剔除显示过的指标
        }

    }


// ++++++++++ 宽窄皆有函数 ++++++++++
    // 选择第三方登陆
    function A_Login(){
        $('body').on('click', '#login,[data-login]', function(){
            var i=$(this),t=i.attr('data-title')||'登陆',u=i.attr('data-get')?'?'+i.attr('data-get'):'',w=$WIN_SMALL?220:600;
            layer.open({type:2,title:t,shadeClose:true,area:[w+'px','300px'],content:['/Team/login.php'+u,'no'] });
        });
    };
    // 退出
    function A_Logout(){
        $('#logout').on('click',function(){
            layer.msg('确定退出登录状态？',{btn:['确定','取消'],time:0,shadeClose:true,yes:function(index){
                    layer.close(index);
                    $.ajax({url:'/Team/Centre/logout.php',
                        beforeSend:function(){ layer.load();},
                        success:function(data){
                            layer.closeAll('loading');
                            if(data=='ok'){layer.alert('成功退出登录！',{icon:1},function(index){window.location.reload();layer.close(index)})}
                            else{layer.alert('出现错误！',{icon:2},function(index){window.location.reload();layer.close(index)})}
                    }})
                }
            });
        });
    };
    // 页面底部
    function A_WebInfo(){
        $('#webinfo dt').on('click', function(){ layer.open({ type:1,title:$(this).text(),content:$(this).next('dd'),shadeClose:true});});
    };
    // 预览小图，开大图
    function A_PopBigImg(){
        $('body').on('click', '[data-popbigimg]', function(){
            var i=$(this),t=i.attr('alt'),u=i.attr('data-popbigimg');
            layer.open({type:1,title:t,shadeClose:true,content:'<img alt="'+t+'" src="'+u+'">'});
        });
    };
    // 图书，图片页的浏览
    function A_TuShu_Page(){
        var i=$('#tushu-page-img');
        if(!i.length) return;
        i.css('cursor','pointer');
        var di=$('#tushu-imgpage-viewer');
            di.css({'min-height':'auto','padding':'1em'}); //没有点击时，高度自动

        i.on('click', function(){
            var wh = $WIN_SMALL ? '100%' : 700;
            di.css({'height':wh,'width':wh,'padding':'0','border':'0'});
            // layer.open({type:1,title:i.attr('alt'),area:['auto','auto'],shadeClose:true,content:di});
            i.viewer({ inline:true,navbar:false,title:false,url:'data-tushupage' });
            i.toggle();
        });
    };
    // 边栏目录 div中，是否有超高( > 180 )的ul
    function A_Sidebar_Small(){
        set_height( $CONTENT_NAV_TIP );
        set_height( $DRUG_SEARCH_BOOK );
        // 检查 .border 中是否有超高的，180
        function set_height(d){
            var u = d.children('ul'),
                a = d.children('a[data-pop]'),
                i = d.attr('id'),
                sh = 180;
            if( d.children('ul').outerHeight()<sh-2 ){ return; }
            u.css('height',sh);
            if( $WIN_SMALL ){ return; }
            // 添加
            d.prepend('<a data-pop="'+i+'" style="position:absolute;z-index:100;right:0;" class="icon i-pop" title="弹出" href="javascript:void(0)"></a>');
            // 绑定
            $SIDEBAR_FIXED.on('click', '[data-pop]', function(){
                var n = $( '#' + $(this).attr('data-pop') );
                layer.open({
                    type: 1,
                    title: n.children('h2').text(),
                    content: n.children('ul'),
                    area: ['auto','70%'],
                    shade: 0,
                    shadeClose: false,
                    resize: true,
                    end: function(){ B_Sidebar_Tip_IsScroll(); }
                });
            });
        }

    };

// ++++++++++ Other ++++++++++

});