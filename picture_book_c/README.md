# Cの絵本 第2版 C言語が好きになる新しい9つの扉
```c
#include<stdio.h>

main()
{
    char a = 'A';
    printf("%c\n", a);
    printf("%d\n", a);
}
#=>
A
65
```
* -char a = “ABC”- 文字型に代入できるのは半角文字1個だけ
→文字列は文字の集まり（配列）ダブルクオーテーションでくくる。
つまり、文字型を配列にしたものが文字列
```c
char s[6] = "Hello"; //最後にNULL文字が入る
char s[] = "Hello";  //[]の中を省略すると自動的に文字数＋1個ぶんのメモリを確保
```
* 文字列への代入に「=」が使えるのは初期化のときだけ。それ以外は`strcpy()`を使う。
```c
#include<stdio.h>
#include<string.h>

main()
{
    char a[] = "Hello";
    printf("%s\n", a);
    strcpy(a, "Bye");
    printf("%s\n", a);
}
#=>
Hello
Bye
```
* “%6.1f”：全体を6桁、小数点を1桁

* 条件式や代入式はそれ自体が値を持っている。
偽（false）・・・ ０
真（true）・・・１
a = 3 ・・・３　代入式では代入した値がその代入式全体の値になる
```c
#include<stdio.h>

main()
{
    int a = 10, b = 20;
    printf("a==b %d \n", a==b);
    printf("a<b %d \n", a<b);
}
#=>
a==b 0
a<b 1
```

* 三項演算子
X = （条件）？ （条件が真のとき）： （条件が偽のとき）
```c
#include<stdio.h>

main()
{
    int a = 40, x;
    x = (10 <= a && a <= 100) ? a : 0;
    printf("%d \n", x);
}
#=>
40
```

* 16進数
 数字の前に「0x」をつける。また書式指定では「%x」を使う。

* キャスト演算子
型名を（）でくくったものを値や変数の前に書くと、型を変換できる。
```c
#include<stdio.h>

main()
{
    printf("3*2=%f\n", 3/(float)2);
}
#=>
3*2=1.500000
```

* if文
if(条件式)
{
ブロック
}
{}でブロックを書くと複数の処理が書けるが、インデントのみでは１つの処理しか書けない。
```c
#include<stdio.h>

main()
{
    int a = 90;
    if(a > 80)
    {
        if(a == 100)
            printf("満点！\n");
        else
            printf("もう少し！\n");
    }
    else
        printf("頑張ろう！\n");
}
#=>
もう少し
```

* for文
int i
for(iの初期値; 条件; インクリメントなど)
※カンマじゃなくてセミコロンなのが注意！
```c
#include<stdio.h>

main()
{
    int i;
    for(i = 0; i < 4; i++)
        printf("%d\n", i);
}

#=>
0
1
2
3
```

* while文
for文との違いは、カウンタがない。主にキーボードからの入力など、繰り返す回数がわからないときに使用する。
Do〜while文では、条件を下に書くことで、初回の実行は必ず処理する。
※getchar()：キーボードからの入力を待つ。
```c
#include<stdio.h>

main()
{
    char a;
    do {
        a = getchar();
        printf("%c", a);
    } while(a != 'e');
}

a
#=> a
hello
#=> he
```
※ breakは一番近いブロックのおわりにジャンプする。
※ continueは繰り返しのその回の処理を中断し、次の回を実行する。

* switch文
複数のcaseから式の値に合うものを選び、その処理を実行。どれにもあてはまらないときはdefaultに進む。
※各caseの最後にはbreak文を記述し、選択した処理のみを行うようにする。
※式には数値のみ（それ以外はif〜else文を使う）
```c
#include<stdio.h>

main()
{
    char a;
    printf("１か２の数字を入力\n");
    a = getchar();

    switch(a)
    {
    case '1':
        printf("中吉\n");
        break;
    case '2':
        printf("大吉\n");
        break;
    default:
        printf("入力が間違っています\n");
    }
}

#=>
１か２の数字を入力
1
中吉
```

* 配列
配列は複数の同じ型の変数を1つにまとめたもの。
```c
int a[4] = {1, 2, 3, 4};
int a[] = {1, 2, 3, 4};  //[]内を省略すると{}内のデータ数から要素数を自動で決定
```

```c
#include<stdio.h>

main()
{
    int i;
    int a[] = {1, 2, 3, 4};
    for(i = 3; i >= 0; i--)
        printf("%d ", a[i]);
}
#=>
4 3 2 1
```

* 文字列の比較
```c
#include<stdio.h>
#include<string.h>

main()
{
    char a[] = "ABC";
    char b[] = "ABD";
    int c = strcmp(a, b);
    printf("%d\n", c);
}
#=>
-1
```

* 多次元配列
```c
#include<stdio.h>

main()
{
    int a[2][3] = {
        {10, 20, 30},
        {40, 50, 60}
    };
    printf("%d\n", a[0][2]);
}
#=>
30
```

* アドレス
メモリには1バイトごとにアドレスがついており、どこにデータが入っているか管理している。
変数名の頭に「&」をつけるとその変数のアドレスを表す。
```c
#include<stdio.h>

main()
{
    char a = 'A';
    printf("%x\n", &a);
}
#=>
58e0da8f
```

* ポインタ
変数のアドレスを値とする変数をポインタという。ポインタには型の区別がある。
ポインタ名に*をつけると、そのポインタが指す先のデータを参照する。
```c
#include<stdio.h>

main()
{
    char x = 4, y;
    char *p = &x;
    y = *p;
    printf("アドレス%xの値は%dです\n", p, y);
}
#=>
アドレス5dc1aa8fの値は4です
```
どこも指していないことをはっきりさせるときはNULLポインタを使う。
`int *p = NULL;`
NULLの値は0になっているため、下記のようにポインタが有効かどうかを調べられる。
`if(p != NULL)` または `if(p)`

* ポインタと配列
配列の名前そのものは配列の最初の要素のポインタの役割
`int a[4];`aはa[0]のポインタの役割
ポインタに対しては整数の加算と引算のみ可能
```c
#include<stdio.h>

main()
{
    int a[4] = {10, 20, 30, 40};
    printf("配列名a：%x\n", a);
    int *p = a + 2;
    printf("%d\n", *p);
    printf("%d\n", *(a + 2));
}
#=>
配列名a：59801a70
30
30
```

* 動的なメモリ確保
ポインタを用意して、確保したメモリの先頭のアドレスをポインタに格納する。
使わなくなったら解放する。
`malloc`：引数で指定したバイト数のメモリを確保し、先頭のアドレスを返す。
`calloc`：メモリを確保し、要素をすべて０に初期化する。
`realloc`：一度確保したメモリを違うサイズで確保し直す。

```c
#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include<memory.h>

main()
{
    char *b;
    char a[4] = {10, 20, 30, 40};
    b = (char *)malloc(sizeof(char)*200);
    if(!b)  //メモリを確保できなかったときのチェックは必ず行う
        printf("No memory");
    memcpy(b, a, sizeof(char)*4);
    printf("%d %d %d %d\n", b[0], b[1], b[2], b[3]);
    free(b);
}
#=>
10 20 30 40
```

* 関数
```c
#include<stdio.h>

int addnum(int a, int b)
{
    int x = a + b;
    return x;
}

main()
{
    int y = addnum(2, 3);
    printf("%d\n", y);
}
#=>
5
```

* プロトタイプ
プロトタイプ宣言をすると、
・関数呼び出し→関数の定義の順に書いても大丈夫
・プロトタイプ宣言に反する関数を書くとコンパイルエラーになる。
```c
#include<stdio.h>
void dispnum(int);

main()
{
    int x = 10;
    dispnum(5);
    dispnum(x);
}

void dispnum(int a)
{
    printf("値は%d\n", a);
}
#=>
値は5
値は10
```

* ファイル
ファイルには大きく分けてテキストファイルとバイナリファイルの2種類ある。
<テキストファイル>
①対象ファイルを開き、ファイルポインタを得る
②ファイルポインタを通して読み書きする
③ファイルを閉じる
```c
#include<stdio.h>

main()
{
    FILE *fp;  
    char s[20];
    int i = 1;
    fp = fopen("abc.txt", "r");  //①
    if(fp == NULL)  //fopenに失敗するとNULLが返っているためチェックする
        return fp;
    while(1)
    {
        fgets(s, 20, fp);  //② fgetsは1行ずつ読み込む関数
        if(feof(fp))  //feofはファイルの終端でtrueになる関数
            break;
        printf("%d %s", i, s);
        i++;
    }
    fclose(fp);  //③
}
#=>
1 abcde
2 hjklk
3 tyuyu
```
書き出しは”w”でfopenし、下記の関数を使う
`fputs(“aaa”, fp);`
`fprintf(fp, "書式指定", 書き出すデータ)`

<バイナリファイル>
バイナリファイルも開くときには`fopen`を使う。オープンモードで「b」をつける。
読み込みは`fread`・書き込みは`fwrite`
`fread(先頭のアドレス, sizeof(型), 読み込み回数, fp);`

* C言語は入出力のために、`stdin、stdout、stderr`の３つのファイルポインタを用意している。
これは実行と同時に自動で開いて、自動で閉じる。

* キーボード入力
`scanf()`：キーボードから入力したデータを指定の書式に変換して変数に格納
`gets()`：1行分の文字列を文字配列に格納（スペースも読み込める）
`getchar()`：1文字だけを変数に格納

* 構造体
構造体とは複数の型の変数をまとめたもの。構造体によってまとめた要素ひとつひとつのことを*メンバ*という
①構造体テンプレートの宣言
```c
struct data{
    int no;
    char name[10];
    int age;
}
```
②構造体変数の宣言
```c
struct data list1;
```
①、②を同時に宣言
```c
struct data{
    int no;
    char name[10];
    int age;
} list1;
```
構造体変数のメンバを参照するには「.」を使う。
```c
#include<stdio.h>

struct data {
    int no;
    char name[10];
} list;

struct data list = {
    1,
    "chisa"
};

main()
{
    printf("%d歳\n", list.no);
    printf("%s\n", list.name);
}
#=>
1歳
chisa
```

* 構造体のポインタ
```c
#include<stdio.h>

struct data {
    int no;
    char name[10];
} list;

struct data *sp = &list;

main()
{
    sp->no = 1;
    printf("%d歳\n", list.no);
}
#=>
1歳
```

* 構造体の配列
```c
struct data {
    int no;
    char name[10];
} list[10];

struct data list[10] = {
    {1, "aaa"},
    {2, "bbb"}
}
```

* C言語のプログラムの実行ファイルができるには
コンパイルとリンク（併せてビルドまたはメイクという）が必要
コンパイルの前に*プリプロセッサ*がコメントの削除やファイルのインクルードを行う。
→コンパイラにより機会語に翻訳されたオブジェクトファイルができる
→リンカがオブジェクトファイルやライブラリファイルを結合（リンク）して1つの実行ファイルを生成

* マクロ
「#」から始まる1行をマクロと呼び、プリプロセッサが処理する。
