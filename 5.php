<?
    if(isset($_POST['yes']))
    {
        echo "Вы ответили \"Да\", спасибо за ответ<br>";
    }
    
    if(isset($_POST['no']))
    {
        echo "Вы ответили \"Нет\", спасибо за ответ<br>";
    }
?>
Это вопрос, ответьте на него (Да/Нет)
<form action="" method="post">
    <input type="submit" name="yes" value="Да" />&nbsp;<input type="submit" name="no" value="Нет" />
</form>
