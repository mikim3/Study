package com.website.movie.biz.service.impl;

import com.website.movie.biz.service.EmailService;
import lombok.RequiredArgsConstructor;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.stereotype.Service;

import javax.mail.internet.MimeMessage;

@Service
@RequiredArgsConstructor
public class EmailServiceImpl implements EmailService {

    private JavaMailSender javaMailSender;

    public EmailServiceImpl(JavaMailSender javaMailSender) {
        this.javaMailSender = javaMailSender;
    }

    public void sendMail(String toEmail, String subject, String message) throws javax.mail.MessagingException {
        MimeMessage mimeMessage = javaMailSender.createMimeMessage();
        MimeMessageHelper helper = new MimeMessageHelper(mimeMessage, "utf-8");
        
        helper.setFrom("222022팀");  //보내는사람
        helper.setTo(toEmail); //받는사람
        helper.setSubject(subject); //메일제목
        helper.setText(message, true); //true 넣을경우 html

        javaMailSender.send(mimeMessage);
    }
}