#Kokaton Invader

##実行環境の必要条件
*Python >= 3.10
*Pygame >= 2.1

##ゲームの概要
タイトーが開発した「スペースインベーダー」を基にした、侵略してくるインベーダーをこうかとんが迎撃するゲームである。画面上方から迫りくるインベーダーを左右に移動できるビーム砲で打ち、インベーダーを全滅させることを目的とする。時々、上空に敵母艦のUFOが出現し、これを撃ち落とすとボーナス点を獲得できる。

##ゲームの実装

###共通基本機能
*背景画像の描画

###担当追加機能
*こうかとん（担当：合田）：主人公であるこうかとんを生成
*Enemy（担当：遠藤）：(インベーダー)を生成
*敵の動き（担当：遠藤）：Enemyが左右に動き、徐々に下に降りてくるような動きを作成
*グループ（担当：山田）：敵のグループを管理するクラスを作成
*ビーム（担当：井上）：ビームを出して撃ち落とす機能を作成
*ブロック（担当：井上）：敵とこうかとんの間にブロックするような長方形を作成
*ボーナス敵（担当：井上）：敵の中でも一番強い母艦を生成（他の敵とは違う動きとした）
*テキスト（担当：井上）：ゲーム内で使用するテキストを作成
*残機設定（担当：井上）：こうかとんの残機の設定
*爆発機能（担当：中西）：ビームが当たった時に爆発する機能を作成
*その他（担当：中西）：タイトル画面、ゲーム内音声などを作成

###ToDo

###メモ

