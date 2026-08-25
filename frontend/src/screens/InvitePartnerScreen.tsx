import * as Clipboard from "expo-clipboard";
import { StatusBar } from "expo-status-bar";
import { useState } from "react";
import {
  Platform,
  Pressable,
  SafeAreaView,
  Share,
  StyleSheet,
  Text,
  View,
} from "react-native";
import { ClockIcon } from "../components/icons/ClockIcon";
import { CopyIcon } from "../components/icons/CopyIcon";
import { ShareIcon } from "../components/icons/ShareIcon";
import { colors } from "../theme/colors";

const INVITE_CODE = "ABC123";

type Props = {
  inviteCode?: string;
};

export function InvitePartnerScreen({ inviteCode = INVITE_CODE }: Props) {
  const [copied, setCopied] = useState(false);
  const prefix = inviteCode.slice(0, 3);
  const suffix = inviteCode.slice(3);

  const handleCopy = async () => {
    await Clipboard.setStringAsync(inviteCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleShare = async () => {
    try {
      await Share.share({
        message: `Join me on forkeeps with invite code ${inviteCode}`,
      });
    } catch {
      // User dismissed share sheet — ignore.
    }
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar style="dark" />
      <View style={styles.screen}>
        <View style={styles.header}>
          <Text style={styles.title}>Invite your partner</Text>
          <Text style={styles.subtitle}>
            Share this code with your partner to connect your accounts.
          </Text>
        </View>

        <View style={styles.codeCard}>
          <View style={styles.codeLabelRow}>
            <View style={styles.sageDot} />
            <Text style={styles.codeLabel}>Invite Code</Text>
            <View style={styles.sageDot} />
          </View>

          <Text style={styles.codeValue}>
            <Text style={styles.codePrefix}>{prefix}</Text>
            <Text style={styles.codeSuffix}>{suffix}</Text>
          </Text>

          <View style={styles.validityBadge}>
            <View style={styles.clockIconBox}>
              <ClockIcon size={13} />
            </View>
            <Text style={styles.validityText}>Valid for 24 hours</Text>
          </View>
        </View>

        <Text style={styles.helperText}>
          Your partner uses this code to join your couple space.
        </Text>

        <View style={styles.actions}>
          <Pressable
            accessibilityRole="button"
            onPress={handleCopy}
            style={styles.primaryButton}
          >
            <View style={styles.copyIconBox}>
              <CopyIcon size={17} />
            </View>
            <Text style={styles.primaryButtonText}>
              {copied ? "Copied!" : "Copy Code"}
            </Text>
          </Pressable>

          <Pressable
            accessibilityRole="button"
            onPress={handleShare}
            style={styles.outlineButton}
          >
            <View style={styles.shareIconBox}>
              <ShareIcon size={16} />
            </View>
            <Text style={styles.outlineButtonText}>Share Invite</Text>
          </Pressable>
        </View>
      </View>
    </SafeAreaView>
  );
}

const mono = Platform.select({
  ios: "Menlo",
  android: "monospace",
  default: "monospace",
});

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: colors.background,
  },
  screen: {
    flex: 1,
    paddingHorizontal: 28,
    paddingTop: 11,
    backgroundColor: colors.background,
  },
  header: {
    marginBottom: 15,
  },
  title: {
    color: colors.text,
    fontSize: 28,
    lineHeight: 34,
    fontWeight: "800",
    letterSpacing: -0.75,
    marginBottom: 10,
  },
  subtitle: {
    color: colors.mutedText,
    fontSize: 15,
    lineHeight: 23,
    fontWeight: "500",
    maxWidth: 364,
  },
  codeCard: {
    width: "100%",
    minHeight: 171,
    borderRadius: 28,
    borderWidth: 1.3,
    borderColor: colors.panelBorder,
    backgroundColor: colors.card,
    alignItems: "center",
    paddingTop: 24,
    paddingBottom: 19,
    paddingHorizontal: 22,
    gap: 15,
    shadowColor: colors.text,
    shadowOpacity: 0.07,
    shadowRadius: 11,
    shadowOffset: { width: 0, height: 4 },
    elevation: 3,
    marginBottom: 15,
  },
  codeLabelRow: {
    flexDirection: "row",
    alignItems: "center",
    gap: 6,
  },
  sageDot: {
    width: 5,
    height: 5,
    borderRadius: 2.5,
    backgroundColor: colors.sage,
  },
  codeLabel: {
    color: colors.quietText,
    fontSize: 10,
    lineHeight: 15,
    fontWeight: "500",
    letterSpacing: 1.6,
    textTransform: "uppercase",
    fontFamily: mono,
  },
  codeValue: {
    fontSize: 47,
    lineHeight: 47,
    letterSpacing: 8.6,
    fontFamily: mono,
  },
  codePrefix: {
    color: colors.text,
  },
  codeSuffix: {
    color: colors.primary,
  },
  validityBadge: {
    flexDirection: "row",
    alignItems: "center",
    gap: 5,
    paddingHorizontal: 14,
    paddingVertical: 5,
    borderRadius: 22,
    backgroundColor: colors.softCoralBadge,
    borderWidth: 0.9,
    borderColor: "rgba(232, 122, 109, 0.15)",
  },
  clockIconBox: {
    width: 13,
    height: 13,
  },
  validityText: {
    color: colors.primary,
    fontSize: 12,
    lineHeight: 19,
    fontWeight: "600",
  },
  helperText: {
    color: colors.quietText,
    fontSize: 13,
    lineHeight: 20,
    fontWeight: "500",
    textAlign: "center",
    marginBottom: 22,
  },
  actions: {
    gap: 13,
  },
  primaryButton: {
    minHeight: 59,
    borderRadius: 22,
    backgroundColor: colors.primary,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: 9,
    shadowColor: colors.primary,
    shadowOpacity: 0.3,
    shadowRadius: 13,
    shadowOffset: { width: 0, height: 9 },
    elevation: 4,
  },
  copyIconBox: {
    width: 17,
    height: 17,
  },
  primaryButtonText: {
    color: colors.card,
    fontSize: 17,
    lineHeight: 26,
    fontWeight: "800",
    letterSpacing: -0.32,
  },
  outlineButton: {
    minHeight: 58,
    borderRadius: 22,
    borderWidth: 1.3,
    borderColor: colors.border,
    backgroundColor: colors.card,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: 9,
  },
  shareIconBox: {
    width: 16,
    height: 16,
  },
  outlineButtonText: {
    color: colors.text,
    fontSize: 16,
    lineHeight: 24,
    fontWeight: "700",
    letterSpacing: -0.22,
  },
});
