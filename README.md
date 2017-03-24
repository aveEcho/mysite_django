# mysite_django

让我们来看下Django根据我们的模型（model）将会为在数据库中创建的表而执行的SQL代码。sqlmigrate命令带上数据库迁移（migration）的名字将会返回它们的SQL，但不会立即去执行。运行以下命令来看下输出：

    python manage.py sqlmigrate blog 0001

输出类似如下:
    
    BEGIN;
    CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(250) NOT NULL, "slug" varchar(250) NOT NULL, "body" text NOT NULL, "publish" datetime NOT NULL, "created" datetime NOT NULL, "updated" datetime NOT NULL, "status" varchar(10) NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id"));
    CREATE INDEX "blog_post_2dbcba41" ON "blog_post" ("slug");
    CREATE INDEX "blog_post_4f331e2f" ON "blog_post" ("author_id");
    COMMIT;
让我们根据新模型（model）来同步数据库。运行以下的命令来应用已存在的数据迁移（migrations）：
    
    python manage.py migrate