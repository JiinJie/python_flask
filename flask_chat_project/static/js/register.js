// 注册功能前端校验
function ClickCaptcha(){
    $("#button-send-captcha").on("click",function(event){
        var $this = $(this);  //将点击的元素作为变量
        var email = $("input[name='email']").val();
        if(!email){
            alert("请先输入邮箱！");
//            return;
        }
        //如果有邮箱则通过ajax（Async JavaScript And XML）发送网络请求给后端
        $.ajax({
            url: "/user/captcha",
            method: "POST",
            data: {
                "email": email
            },
            //如果返回参数，则使用这个随机验证码与用户输入的进行校验
            success: function(res){
            var code = res['code'];
            if(code == 200){
            //取消点击事件，防止用户多次点击该按钮
                $this.off("click")
            //开始倒计时（使用js内置的定时器）
                var countTime = 60;
                var timer = setInterval(function(){
                countTime -= 1   //从59开始计时
                    if(countTime > 0){
                      $this.text(countTime+"秒后可以重新发送");
                    }else{
                    $this.text("获取验证码");
                    //倒计时结束可以重新点击操作
                    ClickCaptcha();
                    clearInterval(timer)  //清除定时器，不再倒计时
                    }
                    //countTime -= 60   从60开始计时
                },timeout=1000)
                alert("验证码发送成功！");
            }else{
                alert(res['text']);  //使用后端返回的信息
            }

            }
        })
    });
}
//使用$命名的方法会等待网页元素全部加载完成后才会执行
$(function(){
    ClickCaptcha();

});
