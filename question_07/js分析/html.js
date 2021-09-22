function type(a) {
    return null == a ? a + "" : "object" == typeof a || "function" == typeof a ? h[i.call(a)] || "object" : typeof a
}

function s(a) {
    var b = "length" in a && a.length
        , c = type(a);
    return "function" === c || n.isWindow(a) ? !1 : 1 === a.nodeType && b ? !0 : "array" === c || 0 === b || "number" == typeof b && b > 0 && b - 1 in a
}

function each(a, b, c) {
    var d, e = 0, f = a.length, g = true;
    if (c) {
        if (g) {
            for (; f > e; e++)
                if (d = b.apply(a[e], c),
                d === !1)
                    break
        } else
            for (e in a)
                if (d = b.apply(a[e], c),
                d === !1)
                    break
    } else if (g) {
        for (; f > e; e++)
            if (d = b.call(a[e], e, a[e]),
            d === !1)
                break
    } else
        for (e in a)
            if (d = b.call(a[e], e, a[e]),
            d === !1)
                break;
    return a
}

function get_html(data) {
    // if (page) {
    // } else {
    //     page = 1
    // }
    var page = 1
    ttf = data.woff;
    // $('.font').text('').append('<style type="text/css">@font-face { font-family:"fonteditor";src: url(data:font/truetype;charset=utf-8;base64,' + ttf + '); }</style>');
    data = data.data;
    let html = '';
    let mad = `<tr><td><span class="ranking-li-span-1"></span></td><td><!--<img class="ranking-li-img-1"src="//ossweb-img.qq.com/images/lol/img/profileicon2/profileicon3018.jpg"alt="玩家头像">--><span class="ranking-li-span-3">九不想乖</span></td><td><span class="ranking-li-span-4"><img src="//ossweb-img.qq.com/images/lol/space/rank/2019pre/season_2019_challenger.png"alt="段位">最强王者Ⅰ</span></td><td><span class="ranking-li-span-5 fonteditor">random_rank_number</span></td><td><span class="ranking-li-span-6">random_level</span></td><td><span class="ranking-li-span-7"><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a></span></td><td><div class="m-ranking-winrate-2"><!--i的width属性等于胜率--><i class="u-ranking-winrate-i"id="ranking_4"data-win="win_rank"style="width: win_rank;"></i><a class="u-winrate ">win_rank</a><a class="u-playnumber">win_number</a></div></td></tr>`;
    let yyq = 1;
    let img_num = 1;
    let imgnum_arr = [1, 8, 3, 2, 4, 5, 7, 5, 15, 3, 9, 8, 5, 1, 3];
    let level_arr = [1, 4, 3, 2, 9, 15];
    let name = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵'];
    each(data, function (index, val) {
        let ppo = mad;
        for (let imgnum = 1; imgnum <= 5; imgnum++) {
            ppo = ppo.replace('img_number', yyq * page + imgnum_arr[imgnum])
        }
        html += ppo.replace('九不想乖', name[yyq + (page - 1) * 10]).replace('win_number', imgnum_arr[yyq] * level_arr[page] * 88 + '场').replace(/win_rank/g, imgnum_arr[yyq] + 60 + level_arr[page] + '%').replace('random_level', imgnum_arr[yyq] * level_arr[page] + 100 * level_arr[page]).replace('img_number', yyq * page).replace('random_rank_number', val.value.replace(/ /g, '') + 'LP');
        yyq += 1;
        img_num += 1
    });

    console.log(html);
}


var data = {
    "woff": "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",
    "status": "1",
    "state": "success",
    "data": [{"value": "&#xe279 &#xb827 &#xe279 &#xc453 "}, {"value": "&#xc697 &#xb721 &#xa865 &#xe937 "}, {"value": "&#xe279 &#xe237 &#xc697 &#xe193 "}, {"value": "&#xe193 &#xc697 &#xc697 &#xb721 "}, {"value": "&#xa687 &#xb721 &#xe279 &#xa687 "}, {"value": "&#xe193 &#xe193 &#xe237 &#xe193 "}, {"value": "&#xb827 &#xe937 &#xe237 &#xb721 "}, {"value": "&#xe193 &#xa865 &#xb721 &#xb721 "}, {"value": "&#xa865 &#xc697 &#xb721 &#xb721 "}, {"value": "&#xa687 &#xa865 &#xa687 &#xe193 "}]
}

get_html(data)
