# How to send email announcements

1. Create a [new email issue](https://github.com/virtualscienceforum/virtualscienceforum/issues/new?labels=email&template=email.md) from template.
2. Select the appropriate subject and "from" fields.
   "From" may be anything at all, but it's better to use something `@virtualscienceforum.org` so that the recipients aren't surprised.
3. Select the recipients. `vsf-announce` is the general mailing list, `speakers_corner` is the speaker's corner one. If you are emailing attendees of a zoom meeting plug in the zoom meeting number.
4. Write the email body. Use [markdown syntax](https://guides.github.com/features/mastering-markdown/).
  - Leave the `%recipient_name%` in place (it will be subsctituted automatically.
  - If you are emailing attendees of a speakers' corner talk, you may insert any of the variables defined in the [talks_file](speakers_corner_talks.yml) surrounded by double figure brackets. For example you may write `the talk title is: {{title}}`.
  - If you want to email meeting particpants their registration link, use `%recipient.join_url%`, for example as `you can join using your [registration link](%recipient.join_url%)`.
5. Open the issue.
6. Once another VSF team member vets the email contents, they add the "approved" label, and the email is sent.
