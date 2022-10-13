//判断account是邮箱还是用户名提交参数
function ClickChangeName(){
        var account = $("input[id='InputAccount']").val();
        console.log(account)
        document.write(account)
        //window.alert(account)
        if(account.search(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/) != -1){
            document.getElementById('InputAccount').name='email';
        }else{
            document.getElementById('InputAccount').name='username';
        }
        //return False;
    }

// $(function(){
//     ClickChangeName();

// });